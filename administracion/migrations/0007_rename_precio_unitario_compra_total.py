# Generated by Django 5.1.3 on 2024-11-18 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_rename_precio_total_venta_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='precio_unitario',
            new_name='total',
        ),
    ]
