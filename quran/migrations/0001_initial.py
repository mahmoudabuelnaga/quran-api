# Generated by Django 4.0.4 on 2022-06-29 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('name_ar', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recitations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=250)),
                ('name_ar', models.CharField(max_length=250)),
                ('read_surat_link', models.URLField()),
                ('download_surat_link', models.URLField()),
                ('surat_time', models.CharField(max_length=100)),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recitations', to='quran.reader')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
