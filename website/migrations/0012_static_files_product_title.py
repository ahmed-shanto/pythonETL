# Generated by Django 4.1.4 on 2023-01-31 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_rename_type_vacancy_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='static_files',
            name='product_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
