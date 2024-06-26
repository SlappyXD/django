# Generated by Django 4.1.7 on 2023-12-31 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0022_alter_categoria_fecharegistro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='detallenotaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='detalleordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='detallepedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='documentocompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='documentoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='notaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='pedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='tipocliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 12, 30, 23, 19, 41, 268746)),
        ),
    ]
