# Generated by Django 2.1 on 2019-02-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_report', '0004_report_punish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='punish',
            field=models.DurationField(),
        ),
    ]
