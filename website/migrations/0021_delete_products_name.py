# Generated by Django 4.1.4 on 2023-01-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_rename_p_name_products_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products_Name',
        ),
    ]
