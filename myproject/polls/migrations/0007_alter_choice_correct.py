# Generated by Django 3.2.3 on 2021-07-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_choice_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='correct',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
