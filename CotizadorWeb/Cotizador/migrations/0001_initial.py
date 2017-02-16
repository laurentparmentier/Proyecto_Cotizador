# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(choices=[('CAD', 'CAD SPORT'), ('ORA', 'ORANGE SPORT'), ('GOL', 'GOLDEP')], max_length=3)),
                ('cliente', models.CharField(max_length=120)),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_cotizacion', models.DateField()),
                ('observaciones', models.TextField(default='Precios sujetos a cambios sin previo aviso.')),
                ('iva', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('subtotal', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=240)),
                ('precio_unitario', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('cantidad', models.IntegerField(default=1)),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cotizador.cotizacion')),
            ],
        ),
    ]
