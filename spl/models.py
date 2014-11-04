from django.db import models

from jsonfield import JSONField


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

    id = models.CharField('Code', max_length=100, primary_key=True)
    code_system = models.CharField('Code System', max_length=200, null=True, blank=True)
    name = models.CharField('Name', max_length=300)
    class_code = models.CharField('Class Code', max_length=100, null=True, blank=True)

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

    def __unicode__(self):
        return self.title


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

    def __unicode__(self):
        return self.medicine_name


class SPLData(CommonInfo):

    # Extracted from DailyMed
    setid                   = models.CharField('setid', max_length=40, unique=True)
    setid_product           = models.CharField('setid_product', max_length=100)
    splsize                 = JSONField('SPLSIZE')
    splshape                = JSONField('SPLSHAPE')
    splscore                = JSONField('SPLSCORE')
    splimprint              = JSONField('SPLIMPRINT')
    splcolor                = JSONField('SPLCOLOR')
    spl_strength            = models.CharField('SPL_STRENGTH', max_length=100, null=True, blank=True)
    spl_ingredients         = JSONField('SPL_INGREDIENTS')
    spl_inactive_ing        = JSONField('SPL_INACTIVE_ING')
    source                  = models.CharField('source', max_length=100, null=True, blank=True)
    rxtty                   = models.CharField('rxtty', max_length=100, null=True, blank=True)
    rxstring                = models.CharField('rxttystring', max_length=100, null=True, blank=True)
    rxcui                   = models.CharField('rxcui', max_length=100, null=True, blank=True)
    produce_code            = models.CharField('produce_code', max_length=100, null=True, blank=True)
    part_num                = models.CharField('part_num', max_length=100, null=True, blank=True)
    part_medicine_name      = models.CharField('part_medicine_name', max_length=100, null=True, blank=True)
    ndc9                    = models.CharField('ndc9', max_length=100, null=True, blank=True)
    medicine_name           = models.CharField('medicine_name', max_length=100, null=True, blank=True)
    marketing_act_code      = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    effective_time          = models.CharField('effective_time', max_length=100, null=True, blank=True)
    file_name               = models.CharField('file_name', max_length=100, null=True, blank=True)
    equal_product_code      = models.CharField('equal_product_code', max_length=100, null=True, blank=True)
    dosage_form             = models.CharField('dosage_form', max_length=100, null=True, blank=True)
    document_type           = models.CharField('document_type', max_length=100, null=True, blank=True)
    dea_schedule_code       = models.CharField('DEA_SCHEDULE_CODE', max_length=100, null=True, blank=True)
    dea_schedule_name       = models.CharField('DEA_SCHEDULE_NAME', max_length=100, null=True, blank=True)
    author_type             = models.CharField('author_type', max_length=100, null=True, blank=True)
    author_type             = models.CharField('author', max_length=100, null=True, blank=True)
    approval_code           = models.CharField('approval_code', max_length=100, null=True, blank=True)

    # Extracted from other Sources
    image_source            = models.CharField('Image Source', max_length=100, null=True, blank=True)
    image_id                = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    has_image               = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    from_sis                = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    version_number          = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    clinical_setid          = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    unii_code               = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    physical_characteristics= models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    laberer_code            = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    application_number      = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.medicine_name
