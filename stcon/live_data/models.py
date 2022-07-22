from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.urls import reverse

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AddressIp(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.ForeignKey('ListSt', models.DO_NOTHING, db_column='number', to_field='number', blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    port_address = models.IntegerField(blank=True, null=True)
    time_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'address_ip'
        verbose_name = 'Адрес сокета СКЗ'
        verbose_name_plural = 'Адрес сокета СКЗ'
        ordering = ['-time_create']


class ListSt(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.BigIntegerField(unique=True)
    address = models.TextField(blank=True, null=True)
    coordinates = models.CharField(max_length=50, blank=True, null=True)
    numbersim = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'list_st'
        verbose_name = 'Станции катодной защиты'
        verbose_name_plural = 'Станции катодной защиты'
        ordering = ['number']

    def __str__(self):
        return 'Station ' + str(self.number)


    def get_absolute_url(self):
        return reverse('station', kwargs={'st_id': self.number})


class NormelAddressIp(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.ForeignKey('NormelListSt', models.DO_NOTHING, db_column='number', to_field='number', blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    port_address = models.IntegerField(blank=True, null=True)
    time_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'normel_address_ip'


class NormelListSt(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.BigIntegerField(unique=True)
    address = models.TextField(blank=True, null=True)
    coordinates = models.CharField(max_length=50, blank=True, null=True)
    numbersim = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'normel_list_st'

    def get_absolute_url(self):
        return reverse('station_normel', kwargs={'st_id': self.number})


class St20(models.Model):
    id = models.BigAutoField(primary_key=True)
    u = models.FloatField()
    i = models.FloatField()
    p1 = models.FloatField()
    p2 = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'st_20'
        verbose_name = 'Данные СКЗ №20'
        verbose_name_plural = 'Данные СКЗ №20'
        ordering = ['-time_create']

    def __str__(self):
        return 'Data at ' + str(self.time_create)




class St30(models.Model):
    id = models.BigAutoField(primary_key=True)
    u = models.FloatField()
    i = models.FloatField()
    p1 = models.FloatField()
    p2 = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'st_30'
        verbose_name = 'Данные СКЗ №30'
        verbose_name_plural = 'Данные СКЗ №30'
        ordering = ['-time_create']

    def __str__(self):
        return 'Data at ' + str(self.time_create)


class St31(models.Model):
    id = models.BigAutoField(primary_key=True)
    u = models.FloatField()
    i = models.FloatField()
    p1 = models.FloatField()
    p2 = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'st_31'
        verbose_name = 'Данные СКЗ №31'
        verbose_name_plural = 'Данные СКЗ №31'
        ordering = ['-time_create']

    def __str__(self):
        return 'Data at ' + str(self.time_create)


class St32(models.Model):
    id = models.BigAutoField(primary_key=True)
    u = models.FloatField()
    i = models.FloatField()
    p1 = models.FloatField()
    p2 = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'st_32'
        verbose_name = 'Данные СКЗ №32'
        verbose_name_plural = 'Данные СКЗ №32'
        ordering = ['-time_create']

    def __str__(self):
        return 'Data at ' + str(self.time_create)


class St33(models.Model):
    id = models.BigAutoField(primary_key=True)
    u = models.FloatField()
    i = models.FloatField()
    p1 = models.FloatField()
    p2 = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'st_33'
        verbose_name = 'Данные СКЗ №33'
        verbose_name_plural = 'Данные СКЗ №33'
        ordering = ['-time_create']

    def __str__(self):
        return 'Data at ' + str(self.time_create)





class StNormel1(models.Model):
    id = models.BigAutoField(primary_key=True)
    u_in_f1 = models.FloatField()
    u_in_f2 = models.FloatField()
    u_in_f3 = models.FloatField()
    u_out_f1 = models.FloatField()
    u_out_f2 = models.FloatField()
    u_out_f3 = models.FloatField()
    i_in_f1 = models.FloatField()
    i_in_f2 = models.FloatField()
    i_in_f3 = models.FloatField()
    i_out_f1 = models.FloatField()
    i_out_f2 = models.FloatField()
    i_out_f3 = models.FloatField()
    p1 = models.FloatField()
    p2 = models.FloatField()
    p3 = models.FloatField()
    code_error = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'st_normel_1'


class LogsSt(models.Model):
    st_number = models.ForeignKey('ListSt', models.DO_NOTHING, db_column='number', to_field='number')
    code = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title