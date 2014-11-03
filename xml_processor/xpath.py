from __future__ import print_function

# import os
# import sys
# import fnmatch
import time
from collections import OrderedDict

from lxml import etree


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
        self.error = 0
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
                self.tree = etree.parse(path + '/' + filename)
                return True

            except etree.XMLSyntaxError:
                self.error += 1
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
            self.active_tree = self.tree
            output = {}

            output['setid'] = self.get_attribute('t:setId', 'root')
            output['id_root'] = self.get_attribute('t:id', 'root')
            output['title'] = self.get_text('t:title')
            output['effective_time'] = self.get_attribute('t:effectiveTime', 'value')
            output['version_number'] = self.get_attribute('t:versionNumber', 'value')
            output['code'] = self.get_attribute('t:code', 'code')
            output['filename'] = filename
            output['source'] = self.get_source(path)
            output['author'] = self.get_text('t:author/t:assignedEntity/t:representedOrganization/t:name[1]')
            output['author_legal'] = self.get_text('t:legalAuthenticator/t:assignedEntity/t:representedOrganization/' +
                                                   't:name[1]')

            return output

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

            setid = self.get_attribute('t:setId', 'root')

            # Check how many products exists in the document
            products = self.xpath('t:component/t:structuredBody/t:component/' +
                                  't:section/t:subject/t:manufacturedProduct')

            counter = 0

            for product in products:
                part_counter = 1
                self.active_tree = product

                # Check for parts
                parts = self.xpath('t:*/t:part')
                if parts:
                    generic = self.get_generic(counter, setid)
                    for part in parts:
                        output = {}
                        self.active_tree = part
                        output['dosage_form'] = self.get_attribute("t:*//t:formCode[1]", "code")

                        # check if it is oral solid dosage form (OSDF)
                        if output['dosage_form'] not in self.code_checks:
                            self.skip += 1
                            # Move to the next item
                            continue
                        else:
                            output.update(generic)
                            output.update(self.get_specific(part_counter, part=True))
                            output['id'] = self.generate_id(output, part_counter)
                            product_set.append(output)
                            part_counter += 1
                else:
                    output = {}
                    output['dosage_form'] = self.get_attribute("t:*/t:formCode[1]", "code")

                    # check if it is oral solid dosage form (OSDF)
                    if output['dosage_form'] not in self.code_checks:
                        self.skip += 1
                        # Move to the next item
                        continue
                    else:
                        output.update(self.get_generic(counter, setid))
                        output.update(self.get_specific())
                        output['id'] = self.generate_id(output, counter)
                        product_set.append(output)
                        counter += 1

            return product_set

        else:
            return False

    def generate_id(self, output, counter):
        """ Generates unique id for pills """
        return output['setid_id'] + output['product_code'] + str(counter)

    def get_generic(self, counter, setid):
        """ Retrieves the product information shared by multiple products in an XML file """
        output = {}
        output['setid_id'] = setid
        output['product_code'] = self.get_attribute('t:*//t:code[1]', 'code')
        output['ndc9'] = output['product_code'].replace('-', '')
        output['ndc'] = '%s-%s' % (output['product_code'], counter)
        output['equal_product_code'] = self.get_attribute('t:*//t:definingMaterialKind/t:code', 'code')
        output['medicine_name'] = self.get_text('t:*//t:name[1]')

        return output

    def get_specific(self, part_counter=0, part=False):

        output = {}
        output['part_num'] = part_counter
        if part:
            output['part_medicine_name'] = self.get_text('t:*//t:name[1]')

        output['approval_code'] = self.get_attribute('t:*//t:approval/t:code', 'code')
        output['marketing_act_code'] = self.get_attribute('t:*//t:marketingAct/t:statusCode', 'code')
        output['dea_schedule_code'] = self.get_attribute('t:*//t:policy[@classCode="DEADrugSchedule"]/t:code',
                                                         'code')
        output['dea_schedule_name'] = self.get_attribute('t:*//t:policy[@classCode="DEADrugSchedule"]/t:code',
                                                         'displayName')
        output['splscore'] = self.xpath('t:*//t:characteristic/t:code[@code="SPLSCORE"]')[0].getnext().get('value')
        output['splimage'] = ''

        try:
            output['splimprint'] = self.xpath('t:*//t:characteristic/t:code[@code="SPLIMPRINT"]')[0].getnext().text
        except IndexError:
            output['splimprint'] = ''

        try:
            output['splshape'] = self.xpath('t:*//t:characteristic/t:code[@code="SPLSHAPE"]')[0].getnext().get('code')
        except IndexError:
            output['splshape'] = ''

        try:
            output['splsize'] = self.xpath('t:*//t:characteristic/t:code[@code="SPLSIZE"]')[0].getnext().get('value')
        except IndexError:
            output['splsize'] = ''

        colors = self.xpath('t:*//t:characteristic/t:code[@code="SPLCOLOR"]')
        output['splcolor'] = [color.getnext().get('code') for color in colors]

        return output

    def get_source(self, path):
        """ separates source name from them give path """
        path_segments = path.split('/')
        return path_segments[len(path_segments) - 1]

    def get_text(self, search):
        """ searches for the search item using xpath and returns the text of the first time found """
        try:
            code = self.xpath(search)
            return code[0].text
        except IndexError:
            return ''

    def get_attribute(self, search, attribute):
        """ searches for the search item using xpath and returns the given attribute of the first time found """
        try:
            code = self.xpath(search)
            return code[0].get(attribute)
        except IndexError:
            return ''

    def xpath(self, path):
        """ A wrapper for lxml xpath function
        path: the XPATH search string """
        return self.active_tree.xpath(path, namespaces=self.namespaces)


if __name__ == '__main__':

    start = time.time()

    x = XPath()

    d = '../tmp-unzipped/HRX'
    o = x.product_data('cf4a9b57-b31a-4e38-b3fe-fac2c4d2c509.xml', d)
    print(o)
    # x.test('0548145e-6b20-4843-9bcc-cf270ea2f072.xml', d)

    # folders = ['ANIMAL', 'HOMEO', 'HOTC', 'HRX', 'REMAIN']

    # for folder in folders:
    #     d = '../tmp-unzipped/%s' % folder
    #     files = os.listdir(d)

    #     for f in files:
    #         if fnmatch.fnmatch(f, '*.xml'):
    #              # print(f)
    #             print(x.parse_set_info(f, d))
    #             # print('hit:%s | skip:%s | error:%s' % (x.counter, x.skip, x.error), end='\r')

    # print('\nErrors: %s' % x.error)
    # x.parse("0013824B-6AEE-4DA4-AFFD-35BC6BF19D91.xml")
    # x.parse('006572e2-0f86-4be3-81cd-91e230cce852.xml')

    # print x.get_source('../tmp-unzipped/HRX')
    end = time.time()

    print('Time spent : %s seconds' % (end - start))
