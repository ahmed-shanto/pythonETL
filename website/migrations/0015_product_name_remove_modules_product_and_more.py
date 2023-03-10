# Generated by Django 4.1.4 on 2023-01-31 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_product_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_with_title', models.CharField(blank=True, max_length=500, null=True)),
                ('ordering', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.RemoveField(
            model_name='modules',
            name='product',
        ),
        migrations.AddField(
            model_name='modules',
            name='product_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='website.product_name'),
            preserve_default=False,
        ),
    ]
