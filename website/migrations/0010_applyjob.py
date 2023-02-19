# Generated by Django 4.1.4 on 2023-01-31 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_company_details_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('resume', models.FileField(upload_to='static/resumes/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('linked_jobs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applyjob', to='website.vacancy')),
            ],
            options={
                'verbose_name': 'Cantidate Details',
                'verbose_name_plural': 'Cantidate Details',
            },
        ),
    ]
