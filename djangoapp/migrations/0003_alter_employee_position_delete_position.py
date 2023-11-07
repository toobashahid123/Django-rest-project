# Generated by Django 4.2.2 on 2023-10-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_position_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('manager', 'manager'), ('Teacher', 'Teacher'), ('Developer', 'Developer')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
