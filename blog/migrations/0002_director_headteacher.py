# Generated by Django 3.2.5 on 2021-07-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('exeriance', models.IntegerField()),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='blog.school')),
            ],
        ),
        migrations.CreateModel(
            name='HeadTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('experiance', models.IntegerField()),
                ('director', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='blog.director')),
            ],
        ),
    ]
