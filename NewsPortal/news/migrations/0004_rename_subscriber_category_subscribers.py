# Generated by Django 4.0.1 on 2022-02-03 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subscriber',
            new_name='subscribers',
        ),
    ]
