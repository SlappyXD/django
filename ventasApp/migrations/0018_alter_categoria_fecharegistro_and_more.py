# Generated by Django 4.1.6 on 2023-03-04 23:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0017_alter_categoria_fecharegistro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 889285)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 888286)),
        ),
        migrations.AlterField(
            model_name='detallenotaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 894274)),
        ),
        migrations.AlterField(
            model_name='detalleordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 892277)),
        ),
        migrations.AlterField(
            model_name='detallepedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 891278)),
        ),
        migrations.AlterField(
            model_name='documentocompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 895230)),
        ),
        migrations.AlterField(
            model_name='documentoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 895230)),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 889285)),
        ),
        migrations.AlterField(
            model_name='notaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 893276)),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 892277)),
        ),
        migrations.AlterField(
            model_name='pedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 890280)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 890280)),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 891278)),
        ),
        migrations.AlterField(
            model_name='tipocliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 888286)),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 18, 1, 18, 887253)),
        ),
    ]