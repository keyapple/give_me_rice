# Generated by Django 2.2.2 on 2019-08-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bab_app', '0005_post_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='star',
            field=models.IntegerField(default=0),
        ),
    ]