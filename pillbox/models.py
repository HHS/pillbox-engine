from django.db import models


# Abstract Model
class CommonInfo(models.Model):
    is_active = models.BooleanField('Enabled?', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PillBoxData(CommonInfo):

    # Extracted from DailyMed
    setid = models.CharField('setid', max_length=40, unique=True)
    setid_product = models.CharField('setid_product', max_length=100)
    splsize = models.CharField('SPLSIZE', max_length=100, null=True, blank=True)
    splshape = models.CharField('SPLSHAPE', max_length=100, null=True, blank=True)
    splscore = models.CharField('SPLSCORE', max_length=100, null=True, blank=True)
    splimprint = models.CharField('SPLIMPRINT', max_length=100, null=True, blank=True)
    splcolor = models.CharField('SPLCOLOR', max_length=100, null=True, blank=True)
    spl_strength = models.CharField('SPL_STRENGTH', max_length=100, null=True, blank=True)
    spl_ingredients = models.CharField('SPL_INGREDIENTS', max_length=100, null=True, blank=True)
    spl_inactive_ing = models.CharField('SPL_INACTIVE_ING', max_length=100, null=True, blank=True)
    source = models.CharField('source', max_length=100, null=True, blank=True)
    rxtty = models.CharField('rxtty', max_length=100, null=True, blank=True)
    rxstring = models.CharField('rxttystring', max_length=100, null=True, blank=True)
    rxcui = models.CharField('rxcui', max_length=100, null=True, blank=True)
    produce_code = models.CharField('produce_code', max_length=100, null=True, blank=True)
    part_num = models.CharField('part_num', max_length=100, null=True, blank=True)
    part_medicine_name = models.CharField('part_medicine_name', max_length=100, null=True, blank=True)
    ndc9 = models.CharField('ndc9', max_length=100, null=True, blank=True)
    medicine_name = models.CharField('medicine_name', max_length=100, null=True, blank=True)
    marketing_act_code = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    effective_time = models.CharField('effective_time', max_length=100, null=True, blank=True)
    file_name = models.CharField('file_name', max_length=100, null=True, blank=True)
    equal_product_code = models.CharField('equal_product_code', max_length=100, null=True, blank=True)
    dosage_form = models.CharField('dosage_form', max_length=100, null=True, blank=True)
    document_type = models.CharField('document_type', max_length=100, null=True, blank=True)
    dea_schedule_code = models.CharField('DEA_SCHEDULE_CODE', max_length=100, null=True, blank=True)
    dea_schedule_name = models.CharField('DEA_SCHEDULE_NAME', max_length=100, null=True, blank=True)
    author_type = models.CharField('author_type', max_length=100, null=True, blank=True)
    author_type = models.CharField('author', max_length=100, null=True, blank=True)
    approval_code = models.CharField('approval_code', max_length=100, null=True, blank=True)

    # Extracted from other Sources
    image_source = models.CharField('Image Source', max_length=100, null=True, blank=True)
    image_id = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    has_image = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    from_sis = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    version_number = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    clinical_setid = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    unii_code = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    physical_characteristics = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    laberer_code = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    application_number = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Pillbox Data'
        verbose_name_plural = 'Pillbox Data'

    def __unicode__(self):
        return self.medicine_name
