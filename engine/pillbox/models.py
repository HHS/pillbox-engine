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
    setid = models.CharField('spp', max_length=250, unique=True)
    setid_product = models.CharField('setid', max_length=250)
    splsize = models.CharField('splsize', max_length=250, null=True, blank=True)
    pillbox_size = models.CharField('pillbox_size', max_length=250, null=True, blank=True)
    splshape = models.CharField('splshape', max_length=250, null=True, blank=True)
    splshape_text = models.CharField('splshape_text', max_length=250, null=True, blank=True)
    pillbox_shape_text = models.CharField('pillbox_shape_text', max_length=250, null=True, blank=True)
    splscore = models.CharField('splscore', max_length=250, null=True, blank=True)
    pillbox_score = models.CharField('pillbox_score', max_length=250, null=True, blank=True)
    splimprint = models.CharField('splimprint', max_length=250, null=True, blank=True)
    pillbox_imprint = models.CharField('pillbox_imprint', max_length=250, null=True, blank=True)
    splcolor = models.CharField('splcolor', max_length=250, null=True, blank=True)
    splcolor_text = models.CharField('splcolor_text', max_length=250, null=True, blank=True)
    pillbox_color_text = models.CharField('pillbox_color_text', max_length=250, null=True, blank=True)
    spl_strength = models.TextField('spl_strength', null=True, blank=True)
    spl_ingredients = models.TextField('spl_ingredients', null=True, blank=True)
    spl_inactive_ing = models.TextField('spl_inactive_ing', null=True, blank=True)
    source = models.CharField('source', max_length=250, null=True, blank=True)
    rxtty = models.TextField('rxtty', null=True, blank=True)
    rxstring = models.TextField('rxtty', null=True, blank=True)
    rxcui = models.CharField('rxcui', max_length=250, null=True, blank=True)
    rx_update_time = models.DateTimeField('RxNorm Update time', null=True, blank=True)
    produce_code = models.CharField('product_code', max_length=250, null=True, blank=True)
    part_num = models.CharField('part_num', max_length=250, null=True, blank=True)
    part_medicine_name = models.CharField('part_medicine_name', max_length=250, null=True, blank=True)
    ndc9 = models.CharField('ndc9', max_length=250, null=True, blank=True)
    ndc_labeler_code = models.CharField('ndc_labeler_code', max_length=60, null=True, blank=True)
    ndc_product_code = models.CharField('ndc_product_code', max_length=60, null=True, blank=True)
    medicine_name = models.CharField('medicine_name', max_length=250, null=True, blank=True)
    marketing_act_code = models.CharField('marketing_act_code', max_length=250, null=True, blank=True)
    effective_time = models.CharField('effective_time', max_length=250, null=True, blank=True)
    file_name = models.CharField('file_name', max_length=250, null=True, blank=True)
    equal_product_code = models.CharField('equal_product_code', max_length=250, null=True, blank=True)
    dosage_form = models.CharField('dosage_form', max_length=250, null=True, blank=True)
    document_type = models.CharField('document_type', max_length=250, null=True, blank=True)
    dea_schedule_code = models.CharField('dea_schedule_code', max_length=250, null=True, blank=True)
    dea_schedule_name = models.CharField('dea_schedule_name', max_length=250, null=True, blank=True)
    author_type = models.CharField('author_type', max_length=250, null=True, blank=True)
    author = models.CharField('author', max_length=250, null=True, blank=True)
    approval_code = models.CharField('approval_code', max_length=250, null=True, blank=True)

    # Extracted from other Sources
    image_source = models.CharField('image_source', max_length=250, null=True, blank=True)
    splimage = models.FileField('splimage', upload_to='pillbox', max_length=250, null=True, blank=True)
    has_image = models.BooleanField('has_image', default=False)
    epc_match = models.CharField('epc_match', max_length=250, null=True, blank=True)
    version_number = models.CharField('version_number', max_length=250, null=True, blank=True)
    laberer_code = models.CharField('laberer_code', max_length=250, null=True, blank=True)
    application_number = models.CharField('application_number', max_length=250, null=True, blank=True)
    updated = models.BooleanField('updated', default=False)
    stale = models.BooleanField('stale', default=False)
    new = models.BooleanField('new', default=False)
    has_pillbox_value = models.BooleanField('Pillbox Value', default=False)

    class Meta:
        verbose_name = 'Pillbox Data'
        verbose_name_plural = 'Pillbox Data'

    def save(self, *args, **kwargs):
        pillbox_fields = PillBoxData._meta.get_all_field_names()

        self.has_pillbox_value = False
        for field in pillbox_fields:
            if 'pillbox_' in field and getattr(self, field):
                self.has_pillbox_value = True
                break

        if self.image_source != '' and self.image_source != 'SPL':
            self.has_pillbox_value = True

        super(PillBoxData, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.medicine_name


class Import(CommonInfo):

    file_name = models.CharField('File Name', max_length=200, null=True, blank=True)
    csv_file = models.FileField('CSV File', upload_to='csv')
    completed = models.BooleanField('Completed?', default=False)
    added = models.IntegerField('Reocrds Added', null=True, blank=True)
    updated = models.IntegerField('Records Updated', null=True, blank=True)
    task_id = models.CharField('Task ID', max_length=200, null=True, blank=True)
    status = models.CharField('Status', max_length=200, null=True, blank=True)
    duration = models.FloatField('Duration (Sec.)', null=True, blank=True)

    class Meta:
        verbose_name = 'Data Import'
        verbose_name_plural = 'Data Import'


class Export(CommonInfo):

    FILE_TYPE = (
        ('json', 'JSON'),
        ('csv', 'CSV'),
        ('yaml', 'YAML'),
        ('xml', 'XML')
    )

    file_type = models.CharField('File Type', max_length=200, choices=FILE_TYPE)
    file_name = models.CharField('File Name', max_length=200)
    export_file = models.FileField('Export File', upload_to='export', null=True, blank=True)
    completed = models.BooleanField('Completed?', default=False)
    task_id = models.CharField('Task ID', max_length=200, null=True, blank=True)
    status = models.CharField('Status', max_length=200, null=True, blank=True)
    duration = models.FloatField('Duration (Sec.)', null=True, blank=True)

    class Meta:
        verbose_name = 'Export'
        verbose_name_plural = 'Export'


class Color(models.Model):

    display_name = models.CharField('SPL Display Name', max_length=250)
    code = models.CharField('SPL Code', max_length=250)
    hex_value = models.CharField('HEX Value', max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.display_name


class Shape(models.Model):

    display_name = models.CharField('SPL Display Name', max_length=250)
    code = models.CharField('SPL Code', max_length=250)

    def __unicode__(self):
        return self.display_name
