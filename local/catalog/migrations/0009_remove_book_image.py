# Generated by Django 4.2.2 on 2023-06-13 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]
