# Generated by Django 4.1.4 on 2023-01-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_company_details_about_count_one_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_count',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
