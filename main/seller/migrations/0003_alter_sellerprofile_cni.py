# Generated by Django 4.2.5 on 2023-09-15 23:31

from django.db import migrations, models
import seller.models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_sellerprofile_phone_number_alter_sellerprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='cni',
            field=models.CharField(max_length=8, validators=[seller.models.cni_validator]),
        ),
    ]
