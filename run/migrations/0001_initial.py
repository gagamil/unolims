# Generated by Django 3.2.7 on 2022-08-31 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('barcodes', models.JSONField()),
                ('run_characteristics', models.JSONField()),
                ('run_xtra_data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='RunResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.JSONField()),
                ('barcode_data', models.JSONField()),
                ('prev', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='run.runresult')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='run.run')),
            ],
        ),
        migrations.CreateModel(
            name='RunConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('well_template', models.JSONField()),
                ('run_file', models.FileField(upload_to='')),
                ('run', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='run.run')),
            ],
        ),
    ]
