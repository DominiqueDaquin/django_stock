# Generated by Django 3.2.19 on 2023-08-13 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pannier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleid', models.IntegerField()),
                ('quantite', models.IntegerField()),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientpage.compte')),
            ],
        ),
    ]
