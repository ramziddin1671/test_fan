# Generated by Django 3.2.3 on 2021-07-12 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='user',
            new_name='user_id',
        ),
    ]
