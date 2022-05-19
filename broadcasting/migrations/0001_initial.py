# Generated by Django 4.0.4 on 2022-05-19 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcasting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=250)),
                ('riwaya_en', models.CharField(blank=True, max_length=250, null=True)),
                ('title_ar', models.CharField(max_length=250)),
                ('riwaya_at', models.CharField(blank=True, max_length=250, null=True)),
                ('broadcasting', models.URLField()),
                ('status_type', models.CharField(choices=[('reading', 'Reading'), ('science', 'Science and Interpretation'), ('translators', 'Translators')], default='reading', max_length=20)),
            ],
            options={
                'ordering': ('status_type',),
            },
        ),
    ]
