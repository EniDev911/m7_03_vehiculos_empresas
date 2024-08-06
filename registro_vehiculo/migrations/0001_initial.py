# Generated by Django 5.0.7 on 2024-08-06 00:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vehiculo",
            fields=[
                (
                    "patente",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("marca", models.CharField(max_length=20)),
                ("modelo", models.CharField(max_length=20)),
                ("year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RegistroContabilidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_compra", models.DateField()),
                ("valor", models.FloatField()),
                (
                    "vehiculo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registro_vehiculo.vehiculo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Chofer",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("activo", models.BooleanField(default=False)),
                ("creacion_registro", models.DateField(auto_now=True)),
                (
                    "vehiculo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registro_vehiculo.vehiculo",
                    ),
                ),
            ],
        ),
    ]
