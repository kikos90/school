from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField

class School(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    TYPE_SCHOOL = [
        ('1', "Средняя"),
        ('2', "Гимназия"),
        ('3', "Лицей"),
        ('4', "Частные"),
        ('5', "Интернаты"),
        ('6', "Спорт Школы"),
    ]
    type = models.CharField(max_length=255, choices=TYPE_SCHOOL, default='Школа')

    def __str__ (self):
        return f'{self.name}'

class Director(models.Model):
    name = models.CharField(max_length=255)
    experiance = models.IntegerField()
    school = models.OneToOneField(School, on_delete=models.PROTECT)

    def __str__ (self):
        return f'{self.name}'

class HeadTeacher(models.Model):
    name = models.CharField(max_length=255)
    experiance = models.IntegerField()
    director = models.OneToOneField(Director, on_delete=models.PROTECT)
    school = models.OneToOneField(School, on_delete=models.PROTECT)

    def __str__ (self):
        return f'{self.name}'

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    lesson = models.CharField(max_length=255)
    classes = models.CharField(max_length=255)
    school = models.OneToOneField(School, on_delete=models.PROTECT)
    director = models.OneToOneField(Director, on_delete=models.PROTECT)
    headteacher = models.OneToOneField(HeadTeacher, on_delete=models.PROTECT)

    def __str__ (self):
        return f'{self.name}'

class Students(models.Model):
    name = models.CharField(max_length=255)
    classes = models.CharField(max_length=255)
    school = models.OneToOneField(School, on_delete=models.PROTECT)
    director = models.OneToOneField(Director, on_delete=models.PROTECT)
    headteacher = models.OneToOneField(HeadTeacher, on_delete=models.PROTECT)
    teacher = models.OneToOneField(Teacher, on_delete=models.PROTECT)

    def __str__ (self):
        return f'{self.name}'


