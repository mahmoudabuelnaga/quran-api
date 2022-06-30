# Generated by Django 4.0.4 on 2022-06-29 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_ar', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categorios',
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_ar', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='containers', to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bismillah', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.TextField()),
                ('surat', models.CharField(blank=True, max_length=50, null=True)),
                ('looper', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='categories.container')),
            ],
        ),
    ]