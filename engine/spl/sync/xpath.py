from __future__ import print_function
from os.path import join
import shutil
import time
import re
from collections import OrderedDict

from lxml.etree import XMLParser, parse, XMLSyntaxError
from django.conf import settings
from spl.download import check_create_folder


class XPath(object):

    def __init__(self):

        # Check all XMLs against form codes, discard all XMLs that don't match
        self.code_checks = [
            "C25158", "C42895", "C42896",
            "C42917", "C42902", "C42904",
            "C42916", "C42928", "C42936",
            "C42954", "C42998", "C42893",
            "C42897", "C60997", "C42905",
            "C42997", "C42910", "C42927",
            "C42931", "C42930", "C61004",
            "C61005", "C42964", "C42963",
            "C42999", "C61006", "C42985",
            "C42992"
        ]

        self.tree = None
        self.active_tree = None
        self.counter = 0
        self.skip = 0
        self.error = []
        self.namespaces = {'t': 'urn:hl7-org:v3'}
        self.output = OrderedDict()
        self.collection = []
        self.all_action = False

        # self.xml_source = '../tmp-unzipped/HRX'
        # self.xml_source = '../tmp-unzipped/ANIMAL'

    def parse(self, filename, path):
        """ Parses the XML Document """
        if not self.all_action:
            try:
                p = XMLParser()
                self.tree = parse(path + '/' + filename, parser=p)
                return True

            except XMLSyntaxError as e:
                self.error.append({
                    'type': 'XML Syntax Error',
                    'path': path,
                    'filename': filename,
                    'message': e.message
                })
                return False
        else:
            return True

    def all(self, filename, path):
        """ Extract both product and pill info from an xml file """

        # Parse XML Document
        if self.parse(filename, path):
            self.all_action = True
            result = {
                'products': self.products(filename, path),
                'pills': self.pills(filename, path)
            }
            self.all_action = False

            return result
        else:
            return False

    def products(self, filename, path):
        """ This method retrieves the generic data on top of each XML files.
        The goal is to produce the following data:

        setid, id_root, title, effective_time, version_number, code, filename, source, author, author_legal

        The method outputs the result in form of a dictionary with above given keys and relevant values
        """

        # Parse XML Document
        if self.parse(filename, path):

            try:
                self.active_tree = self.tree
                output = {}

                output['setid'] = self._get_attribute('t:setId', 'root')
                output['id_root'] = self._get_attribute('t:id', 'root')
                output['title'] = self._get_text('t:title')
                output['effective_time'] = self._get_attribute('t:effectiveTime', 'value')
                output['version_number'] = self._get_attribute('t:versionNumber', 'value')
                output['code'] = self._get_attribute('t:code', 'code')
                output['filename'] = filename
                output['source'] = self._get_source(path)
                output['author'] = self._get_text('t:author/t:assignedEntity/t:representedOrganization/t:name[1]')
                output['author_legal'] = self._get_text('t:legalAuthenticator/t:assignedEntity/t:representedOrganization' +
                                                        '/t:name[1]')
                output['discontinued'] = False

                return output
            except TypeError as e:
                self.error.append({
                    'type': 'XML Syntax Error',
                    'path': path,
                    'filename': filename,
                    'message': e.message
                })

                return False
        else:
            return False

    def pills(self, filename, path):
        """ Retrieves product data from each XML file.
        returns a list containing all the products in an XML file
        The fields it covers: id, setid, dosage_form, ndc, ndc9, product_code, equal_product_code, approval_code,
        medicine_name,  dea_schedule_code, dea_schedule_name,
        marketing_act_code, splcolor, splsize, splshape, splimprint, splimage, splscore


        part_num, part_medicine_name

        """

        product_set = []

        # Parse XML Document
        if self.parse(filename, path):

            self.active_tree = self.tree

            setid = self._get_attribute('t:setId', 'root')

            # Check how many products exists in the document
            products = self._xpath('t:component/t:structuredBody/t:component/' +
                                   't:section/t:subject/t:manufacturedProduct')
            counter = 0

            for product in products:
                part_counter = 1
                self.active_tree = product

                # Check for parts
                parts = self._xpath('t:*/t:part')
                if parts:
                    generic = self._get_generic(counter, setid)
                    for part in parts:
                        output = {}
                        self.active_tree = part
                        output['dosage_form'] = self._get_attribute("t:*//t:formCode[1]", "code")

                        # check if it is oral solid dosage form (OSDF)
                        if output['dosage_form'] not in self.code_checks:
                            self.skip += 1
                            # Move to the next item
                            continue
                        else:
                            output.update(generic)
                            output.update(self._get_specific(path, part_counter, part=True))
                            output['ssp'] = self._generate_id(output, part_counter)
                            output['ingredients'] = self._get_ingredients()
                            product_set.append(output)
                            part_counter += 1
                else:
                    output = {}
                    output['dosage_form'] = self._get_attribute("t:*/t:formCode[1]", "code")

                    # check if it is oral solid dosage form (OSDF)
                    if output['dosage_form'] not in self.code_checks:
                        self.skip += 1
                        # Move to the next item
                        continue
                    else:
                        output.update(self._get_generic(counter, setid))
                        output.update(self._get_specific(path))
                        output['ssp'] = self._generate_id(output)
                        output['ingredients'] = self._get_ingredients()
                        product_set.append(output)
                        counter += 1

            return product_set

        else:
            return False

    def _get_ingredients(self):
        """ Extract ingredients information from the given XML file
        produces an output similar to this:
        {
            "active_moiety_names": ["ETHINYL ESTRADIOL"],
            "dominator_unit": "1",
            "dominator_value": "1",
            "ingredient_type": "active",
            "numerator_unit": "mg",
            "numerator_value": "0.025",
            "substance_code": "423D2T571U",
            "substance_name": "ETHINYL ESTRADIOL"
        }
        """

        ingredients = self._xpath('t:*//t:ingredient')
        output = {
            'active': [],
            'inactive': []
        }

        for item in ingredients:
            ingredient = {}
            ingredient['class_code'] = item.get('classCode')
            subs = item.getchildren()
            for sub in subs:
                if self._simple_tag(sub.tag) == 'quantity':
                    numerator = self._xpath_with_tree(sub, 't:numerator')[0]
                    denominator = self._xpath_with_tree(sub, 't:denominator')[0]
                    ingredient['active'] = True
                    ingredient['denominator_unit'] = denominator.get('unit')
                    ingredient['denominator_value'] = denominator.get('value')
                    ingredient['numerator_unit'] = numerator.get('unit')
                    ingredient['numerator_value'] = numerator.get('value')
                else:
                    code = self._xpath_with_tree(sub, 't:code')[0]
                    ingredient['id'] = code.get('code')
                    ingredient['code_system'] = code.get('codeSystem')
                    ingredient['name'] = self._xpath_with_tree(sub, 't:name')[0].text
                    active_moieties = self._xpath_with_tree(sub, 't:activeMoiety/t:activeMoiety')
                    if active_moieties:
                        ingredient['active_moieties'] = []
                        for am in active_moieties:
                            children = am.getchildren()
                            ingredient['active_moieties'].append({
                                'id': children[0].get('code'),
                                'name': children[1].text
                            })

            if 'active' in ingredient:
                output['active'].append(ingredient)
            else:
                output['inactive'].append(ingredient)

        return output

    def _generate_id(self, output, part_counter=0):
        """ Generates unique id for pills """
        return output['setid_id'] + '-' + output['produce_code'] + '-' + str(part_counter)

    def _get_generic(self, counter, setid):
        """ Retrieves the product information shared by multiple products in an XML file """
        output = {}
        output['setid_id'] = setid

        manufactured = self._xpath('t:*//t:containerPackagedProduct//t:code')
        if not manufactured:
            manufactured = self._xpath('t:*//t:containerPackagedMedicine//t:code')

        output['product_code'] = [i.get('code') for i in manufactured if i.get('code')][0]
        output['produce_code'] = self._get_attribute('t:*//t:code[1]', 'code')
        if output['produce_code']:
            produce_code_temp = output['produce_code'].split("-")
            output['ndc_labeler_code'] = produce_code_temp[0]
            output['ndc_product_code'] = produce_code_temp[1]
            produce_code_temp[0] = produce_code_temp[0].zfill(5)
            produce_code_temp[1] = produce_code_temp[1].zfill(4)
            output['ndc9'] = produce_code_temp[0] + produce_code_temp[1]
        output['ndc'] = '%s-%s' % (output['produce_code'], counter)
        output['equal_product_code'] = self._get_attribute('t:*//t:definingMaterialKind/t:code', 'code')
        output['medicine_name'] = self._get_text('t:*//t:name[1]')

        return output

    def _get_specific(self, path, part_counter=0, part=False):

        output = {}
        output['part_num'] = part_counter
        if part:
            output['part_medicine_name'] = self._get_text('t:*//t:name[1]')

        output['approval_code'] = self._get_attribute('t:*//t:approval/t:code', 'code')
        output['marketing_act_code'] = self._get_attribute('t:*//t:marketingAct/t:statusCode', 'code')
        output['dea_schedule_code'] = self._get_attribute('t:*//t:policy[@classCode="DEADrugSchedule"]/t:code',
                                                          'code')
        output['dea_schedule_name'] = self._get_attribute('t:*//t:policy[@classCode="DEADrugSchedule"]/t:code',
                                                          'displayName')
        output['splscore'] = self._xpath('t:*//t:characteristic/t:code[@code="SPLSCORE"]')[0].getnext().get('value')
        output['splimage'] = self._get_image(path)

        try:
            output['splimprint'] = self._xpath('t:*//t:characteristic/t:code[@code="SPLIMPRINT"]')[0].getnext().text
        except IndexError:
            output['splimprint'] = ''

        try:
            shape = self._xpath('t:*//t:characteristic/t:code[@code="SPLSHAPE"]')[0].getnext()
            output['splshape'] = shape.get('code')
            # Make sure extra spaces are removed
            output['splshape_text'] = re.sub('[ \f\t\v]$', '', shape.get('displayName').upper())
        except IndexError:
            output['splshape'] = ''
            output['splshape_text'] = ''

        try:
            output['splsize'] = self._xpath('t:*//t:characteristic/t:code[@code="SPLSIZE"]')[0].getnext().get('value')
        except IndexError:
            output['splsize'] = ''

        colors = self._xpath('t:*//t:characteristic/t:code[@code="SPLCOLOR"]')
        try:
            output['splcolor'] = ";".join([color.getnext().get('code') for color in colors])
            output['splcolor_text'] = ";".join([color.getnext().get('displayName') for color in colors]).upper()
        except TypeError:
            pass

        return output

    def _get_image(self, path):

        try:
            image = self._xpath(
                't:*//t:characteristic/t:code[@code="SPLIMAGE"]'
            )[0].getnext().getchildren()[0].get('value')
        except IndexError:
            image = ''

        if image:
            # get source name
            source = self._get_source(path)

            #make sure spl media folder exist
            media_path = check_create_folder(join(settings.MEDIA_ROOT, 'pillbox'))

            #copy image file to the media root if exist
            try:
                source_path = join(join(settings.SOURCE_PATH, source), 'tmp2')
                shutil.copy(join(source_path, image), media_path)
            except IOError:
                pass

            image = 'pillbox/' + image

        return image

    def _get_source(self, path):
        """ separates source name from them give path """
        path_segments = path.split('/')
        return path_segments[len(path_segments) - 1]

    def _get_text(self, search):
        """ searches for the search item using _xpath and returns the text of the first time found """
        try:
            code = self._xpath(search)
            value = code[0].text

            if value:
                # cleanup the values
                # replace spaces more than one with one
                value = re.sub('([\s]{2,})', ' ', value)
                value = value.replace('\n', ' ')
                value = value.replace('\t', ' ')
            else:
                value = 'Value Not Provided'

            return value

        except IndexError:
            return ''

    def _get_attribute(self, search, attribute):
        """ searches for the search item using xpath and returns the given attribute of the first time found """
        try:
            code = self._xpath(search)
            return code[0].get(attribute)
        except IndexError:
            return ''

    def _simple_tag(self, tag):
        """ Removes namespace and returns simple tag
        For example {urn:hl7-org:v3}quantity becomes quantity
        """
        qname = re.compile("{(?P<ns>.*)}(?P<element>.*)")

        m = qname.search(tag)
        return m.groupdict().get("element")

    def _xpath(self, path):
        """ A wrapper for lxml xpath function
        path: the XPATH search string """
        return self.active_tree.xpath(path, namespaces=self.namespaces)

    def _xpath_with_tree(self, tree, path):
        """ Same as _xpath method but only accepts tree too """

        return tree.xpath(path, namespaces=self.namespaces)


def test():

    x = XPath()

    d = join(settings.SOURCE_PATH, 'HOMEO')
    # o = x.pills('0013824B-6AEE-4DA4-AFFD-35BC6BF19D91.xml', d)
    o = x.pills('03e598d8-8da4-2dd0-e054-00144ff88e88.xml', d)
    print(o)

if __name__ == '__main__':

    start = time.time()

    x = XPath()

    d = '../../downloads/unzip/HOTC'
    # o = x.pills('0013824B-6AEE-4DA4-AFFD-35BC6BF19D91.xml', d)
    o = x.pills('03e598d8-8da4-2dd0-e054-00144ff88e88.xml', d)
    print(o)

    end = time.time()

    print('Time spent : %s seconds' % (end - start))
