# Generated by Django 2.2.2 on 2019-06-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20190609_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
