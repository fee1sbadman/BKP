# Generated by Django 2.2.2 on 2019-06-10 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0014_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]
