# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid

from django.db import models


class Department(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, db_comment='')
    name = models.CharField(max_length=100, db_comment='', verbose_name="Наименование")

    class Meta:
        managed = False
        db_table = 'department'
        verbose_name_plural = 'Подразделение'


class DayType(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, db_comment='')
    name = models.CharField(db_column='Name', max_length=100, db_comment='', verbose_name='Наименование')  # Field name made lowercase.
    mark = models.CharField(unique=True, max_length=100, db_comment='', verbose_name='Краткое обозначение')

    class Meta:
        managed = False
        db_table = 'day_type'
        verbose_name_plural = 'Тип дня'
        db_table_comment = ''


class Employee(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, db_comment='')
    name = models.CharField(max_length=100, db_comment='', verbose_name='Имя')
    surname = models.CharField(max_length=100, db_comment='', verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, blank=True, null=True, db_comment='', verbose_name='Отчество')
    email = models.CharField(max_length=100, db_comment='', verbose_name='Почта')
    date_birth = models.DateField(db_comment='', verbose_name='Дата Рождения')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department', db_comment='',
                                   verbose_name='Подразделение')

    class Meta:
        managed = False
        db_table = 'employee'
        verbose_name_plural = 'Сотрудник'
        db_table_comment = 'Сотрудник'


class Timecard(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=100, db_comment='')
    employer = models.ForeignKey(Employee, models.DO_NOTHING, db_comment='', verbose_name='Сотрудник')
    date = models.CharField(max_length=100, db_comment='', verbose_name='Дата')
    day_type = models.ForeignKey(DayType, models.DO_NOTHING, db_comment='', verbose_name='Тип дня')

    class Meta:
        managed = False
        db_table = 'timecard'
        verbose_name_plural = 'Производственный табель'
        db_table_comment = ''
