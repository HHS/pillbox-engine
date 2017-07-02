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
    host = models.CharField('FTP Host', help_text='FTP host to download the files from', max_length=200)
    path = models.CharField('PATH', help_text='Path where the files are located on the ftp server', max_length=200)
    files = JSONField('File Names', help_text='Enter in form python list')
    last_downloaded = models.DateTimeField('Last Downloaded', null=True, blank=True)
    last_unzipped = models.DateTimeField('Last Unzipped', null=True, blank=True)
    zip_size = models.FloatField('Total zip folder size (bytes)', null=True, blank=True)
    unzip_size = models.FloatField('Total unzip folder size (bytes)', null=True, blank=True)
    xml_count = models.IntegerField('Total xml files', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Ingredient(CommonInfo):

    spl_id = models.CharField('Unii Code', max_length=100, unique=True)
    code_system = models.CharField('Code System', max_length=200, null=True, blank=True)
    name = models.CharField('Name', max_length=300)
    class_code = models.CharField('Class Code', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'OSDF Ingredient'

    def __unicode__(self):
        return self.name

class Product(CommonInfo):

    setid = models.CharField('setid', max_length=200, unique=True)
    id_root = models.CharField('id root', max_length=200)
    title = models.TextField('Title', null=True, blank=True)
    effective_time = models.CharField('Effective Time', max_length=100)
    version_number = models.IntegerField('Version Number')
    code = models.CharField('Document Type (Code)', max_length=250)
    filename = models.CharField('File Name', max_length=300)
    source = models.CharField('Source', max_length=250)
    author = models.CharField('Author (Laberer)', max_length=300, null=True, blank=True)
    author_legal = models.CharField('Legal Author', max_length=300, null=True, blank=True)
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


class Pill(CommonInfo):

    ssp = models.CharField('Pillbox Unique ID', max_length=200, unique=True)
    setid = models.ForeignKey(Product)
    dosage_form = models.CharField('Dosage Form', max_length=20)
    ndc = models.CharField('NDC9', max_length=100, null=True, blank=True)
    ndc9 = models.CharField('NDC9', max_length=100, null=True, blank=True)
    product_code = models.CharField('Product Code', max_length=60, null=True, blank=True)
    ndc_labeler_code = models.CharField('ndc_labeler_code', max_length=60, null=True, blank=True)
    ndc_product_code = models.CharField('ndc_product_code', max_length=60, null=True, blank=True)
    produce_code = models.CharField('Produce Code', max_length=60, null=True, blank=True)
    equal_product_code = models.CharField('Equal Product Code', max_length=30, null=True, blank=True)
    approval_code = models.CharField('approval_code', max_length=100, null=True, blank=True)
    medicine_name = models.CharField('Medicine Name', max_length=300, null=True, blank=True)
    part_num = models.IntegerField('Part Number', default=0)
    part_medicine_name = models.CharField('Part Medicine Name', max_length=200, null=True, blank=True)
    rxtty = models.TextField('rxtty', null=True, blank=True)
    rxstring = models.TextField('rxttystring', null=True, blank=True)
    rxcui = models.CharField('rxcui', max_length=100, null=True, blank=True)
    rx_update_time = models.DateTimeField('Time Ended', null=True, blank=True)
    dea_schedule_code = models.CharField('DEA_SCHEDULE_CODE', max_length=100, null=True, blank=True)
    dea_schedule_name = models.CharField('DEA_SCHEDULE_NAME', max_length=100, null=True, blank=True)
    marketing_act_code = models.CharField('MARKETING_ACT_CODE', max_length=100, null=True, blank=True)
    splcolor = models.CharField('SPL Color Code', max_length=100, null=True, blank=True)
    splcolor_text = models.CharField('SPL Color Display Name', max_length=100, null=True, blank=True)
    splsize = models.CharField('SPL Size', max_length=100, null=True, blank=True)
    splshape = models.CharField('SPL Shape Code', max_length=100, null=True, blank=True)
    splshape_text = models.CharField('SPL Shape Display Name', max_length=100, null=True, blank=True)
    splimprint = models.CharField('SPL Imprint', max_length=100, null=True, blank=True)
    splimage = models.FileField('SPL Image', upload_to='spl', max_length=100, null=True, blank=True)
    splscore = models.CharField('SPL Score', max_length=100, null=True, blank=True)
    spl_strength = models.TextField('SPL_STRENGTH', null=True, blank=True)
    spl_ingredients = models.TextField('SPL_INGREDIENTS', null=True, blank=True)
    spl_inactive_ing = models.TextField('SPL_INACTIVE_ING', null=True, blank=True)

    class Meta:
        verbose_name = 'SPL OSDF Pill'
        verbose_name_plural = 'SPL OSDF Pills'

    def __unicode__(self):
        return self.medicine_name


class Task(models.Model):

    name = models.CharField('Task Name', max_length=250)
    task_id = models.CharField('Task ID', max_length=250, null=True, blank=True, unique=True)
    time_started = models.DateTimeField(auto_now_add=True)
    time_ended = models.DateTimeField('Time Ended', null=True, blank=True)
    duration = models.FloatField('Duration', default=0)
    status = models.CharField('Status', max_length=200, null=True, blank=True)
    meta = JSONField('Meta', default={})
    pid = models.CharField('PID', max_length=100, null=True, blank=True)
    is_active = models.BooleanField('Task is active (running)?', default=True)
    download_type = models.CharField('Download source name', max_length=200, null=True, blank=True)
    traceback = models.TextField('Traceback', null=True, blank=True)

    def __unicode__(self):
        return self.name
