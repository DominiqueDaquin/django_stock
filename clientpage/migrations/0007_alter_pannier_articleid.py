# Generated by Django 3.2.19 on 2023-08-15 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20230810_1319'),
        ('clientpage', '0006_auto_20230815_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pannier',
            name='articleid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion.article'),
        ),
    ]