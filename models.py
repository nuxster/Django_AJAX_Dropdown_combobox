from django.db import models
from datetime import date

# Create your models here.
class Device(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, blank=False, null=False, verbose_name="Производитель")
    model = models.ForeignKey('Model', on_delete=models.PROTECT, blank=False, null=False, verbose_name="Модель")
    serial_number = models.CharField(max_length=50, blank=False, null=False, verbose_name="Серийный номер")
    delivery_year = models.DateField(default=date.today, verbose_name="Дата поставки") 
    system = models.ForeignKey('System', on_delete=models.PROTECT, blank=False, null=False, verbose_name="Система")
    to_object = models.ForeignKey('Objects', on_delete=models.PROTECT, blank=False, null=False, verbose_name="Объект")
    responsible = models.ForeignKey('Responsible', on_delete=models.PROTECT, blank=False, null=False, verbose_name="Ответственный")

    # def __str__(self):
    #     return(self.model)
    
    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name="Наименование производителя")

    def __str__(self):
        return(self.name)

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Model(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name="Наименование производителя")
    model = models.CharField(max_length=50, blank=False, null=False, verbose_name="Модель")

    def __str__(self):
        return(self.model)

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Модель устройства'
        verbose_name_plural = 'Модели устройств'

class System(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Системы")

    def __str__(self):
        return(self.name)
    
    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'


class Objects(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Объект")

    def __str__(self):
        return(self.name)
    
    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Responsible(models.Model):
    FIO = models.CharField(max_length=150, blank=False, null=False, verbose_name="ФИО")
    Position = models.CharField(max_length=50, blank=False, null=False, verbose_name="Должность")

    def __str__(self):
        return(self.FIO)

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Ответственный'
        verbose_name_plural = 'Ответственные'
