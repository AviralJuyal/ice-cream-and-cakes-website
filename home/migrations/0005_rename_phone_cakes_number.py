# Generated by Django 3.2.4 on 2021-06-05 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_cakes_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cakes',
            old_name='phone',
            new_name='number',
        ),
    ]
