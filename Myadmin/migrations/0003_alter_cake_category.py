# Generated by Django 3.2.2 on 2021-08-10 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myadmin', '0002_auto_20210810_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myadmin.categorie'),
        ),
    ]
