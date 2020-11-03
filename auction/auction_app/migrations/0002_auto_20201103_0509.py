# Generated by Django 2.1 on 2020-11-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mobile_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
