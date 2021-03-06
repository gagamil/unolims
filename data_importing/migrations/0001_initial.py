# Generated by Django 3.2.7 on 2021-11-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileImportTubeBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_type', models.CharField(choices=[('POOLING_BATCH', 'Pooling batch'), ('RUN_BATCH', 'Run batch')], default='POOLING_BATCH', max_length=32)),
                ('import_file', models.FileField(upload_to='import_batch')),
                ('batch_data', models.JSONField()),
            ],
        ),
    ]
