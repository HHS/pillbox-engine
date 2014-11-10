from django.db import models

# Abstract Model
class CommonInfo(models.Model):
    is_active = models.BooleanField('Enabled?', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Source(CommonInfo):

    title = models.CharField('Title', max_length=100)

    def __unicode__(self):
        return self.title


class Ingredient(CommonInfo):

    id = models.CharField('Unii Code', max_length=100, primary_key=True)
    code_system = models.CharField('Code System', max_length=200, null=True, blank=True)
    name = models.CharField('Name', max_length=300)
    class_code = models.CharField('Class Code', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'OSDF Ingredient'

    def __unicode__(self):
        return self.name


class SetInfo(CommonInfo):

    setid = models.CharField('setid', max_length=200, primary_key=True)
    id_root = models.CharField('id root', max_length=200)
    title = models.TextField('Title', null=True, blank=True)
    effective_time = models.CharField('Effective Time', max_length=8)
    version_number = models.IntegerField('Version Number')
    code = models.CharField('Document Type (Code)', max_length=10)
    filename = models.CharField('File Name', max_length=100)
    source = models.CharField('Source', max_length=20)
    author = models.CharField('Author (Laberer)', max_length=200, null=True, blank=True)
    author_legal = models.CharField('Legal Author', max_length=200, null=True, blank=True)
    is_osdf = models.BooleanField('Is In Oral Solid Dosage Form?', default=False)
    discontinued = models.BooleanField('Is Discontinued from SPL?', default=False)

    class Meta:
        verbose_name = 'SPL Product'
        verbose_name_plural = 'SPL Products'

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.setid


class ProductData(CommonInfo):

    id = models.CharField('id', max_length=200, primary_key=True)
    setid = models.ForeignKey(SetInfo)
    dosage_form = models.CharField('Dosage Form', max_length=20)
    ndc = models.CharField('NDC9', max_length=100, null=True, blank=True)
    ndc9 = models.CharField('NDC9', max_length=100, null=True, blank=True)
    product_code = models.CharField('Product Code', max_length=60, null=True, blank=True)
    equal_product_code = models.CharField('Equal Product Code', max_length=30, null=True, blank=True)
    approval_code = models.CharField('approval_code', max_length=100, null=True, blank=True)
    medicine_name = models.CharField('Medicine Name', max_length=300)
    part_num = models.IntegerField('Part Number', default=0)
    part_medicine_name = models.CharField('Part Medicine Name', max_length=200, null=True, blank=True)
    rxtty = models.CharField('rxtty', max_length=100, null=True, blank=True)
    rxstring = models.CharField('rxttystring', max_length=100, null=True, blank=True)
    rxcui = models.CharField('rxcui', max_length=100, null=True, blank=True)
    dea_schedule_code = models.CharField('DEA_SCHEDULE_CODE', max_length=100, null=True, blank=True)
    dea_schedule_name = models.CharField('DEA_SCHEDULE_NAME', max_length=100, null=True, blank=True)
    marketing_act_code = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    splcolor = models.CharField('SPL Color', max_length=100, null=True, blank=True)
    splsize = models.CharField('SPL Size', max_length=100, null=True, blank=True)
    splshape = models.CharField('SPL Shape', max_length=100, null=True, blank=True)
    splimprint = models.CharField('SPL Imprint', max_length=100, null=True, blank=True)
    splimage = models.CharField('SPL Image', max_length=100, null=True, blank=True)
    splscore = models.CharField('SPL Score', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'SPL OSDF Pill'
        verbose_name_plural = 'SPL OSDF Pills'

    def __unicode__(self):
        return self.medicine_name
