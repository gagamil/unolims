# Generated by Django 3.2.7 on 2021-09-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tubes', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tubebatchposition',
            unique_together={('batch', 'position')},
        ),
    ]
