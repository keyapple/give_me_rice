# Generated by Django 2.2.2 on 2019-08-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bab_app', '0006_comment_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='star_rating',
            field=models.IntegerField(default=0),
        ),
    ]