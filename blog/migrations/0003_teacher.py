# Generated by Django 3.2.5 on 2021-07-03 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_director_headteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lesson', models.CharField(max_length=255)),
                ('classes', models.CharField(max_length=255)),
                ('headteacher', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='blog.headteacher')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='blog.school')),
            ],
        ),
    ]