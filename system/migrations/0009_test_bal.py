# Generated by Django 2.2.2 on 2019-06-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20190607_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='bal',
            field=models.IntegerField(default=0),
        ),
    ]