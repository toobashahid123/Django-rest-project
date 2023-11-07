# Generated by Django 4.2.2 on 2023-10-08 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.type')),
            ],
        ),
    ]
