# Generated by Django 3.2.3 on 2021-07-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210630_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='correct',
            field=models.BooleanField(blank='togri', default='notogri'),
        ),
    ]
