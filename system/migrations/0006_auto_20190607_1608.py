# Generated by Django 2.2.2 on 2019-06-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20190605_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='right_choice',
            field=models.CharField(max_length=10),
        ),
    ]