# Generated by Django 4.0.4 on 2022-06-15 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_prod',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id_producto',
        ),
        migrations.DeleteModel(
            name='venta_producto',
        ),
    ]