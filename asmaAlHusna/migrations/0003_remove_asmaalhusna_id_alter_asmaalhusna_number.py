# Generated by Django 4.0.4 on 2022-05-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asmaAlHusna', '0002_alter_asmaalhusna_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asmaalhusna',
            name='id',
        ),
        migrations.AlterField(
            model_name='asmaalhusna',
            name='number',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]