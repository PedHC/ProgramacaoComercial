# Generated by Django 3.1.2 on 2020-11-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0002_veiculo_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='ano_fabricacao',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='modelo_fabricacao',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='valor',
            field=models.PositiveIntegerField(default=10000),
        ),
    ]
