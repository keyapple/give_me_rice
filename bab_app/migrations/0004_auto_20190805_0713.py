# Generated by Django 2.2.2 on 2019-08-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bab_app', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='amount',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='cooking_level',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='cooking_time',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
