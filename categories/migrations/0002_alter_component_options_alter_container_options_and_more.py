# Generated by Django 4.0.4 on 2022-07-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'ordering': ('number',)},
        ),
        migrations.AlterModelOptions(
            name='container',
            options={'ordering': ('number',)},
        ),
        migrations.AddField(
            model_name='component',
            name='number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='container',
            name='number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]