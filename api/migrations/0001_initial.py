# Generated by Django 4.1.2 on 2022-12-15 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('precio_total', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('especialidad', models.CharField(max_length=25)),
                ('url_imagen', models.CharField(max_length=1000)),
                ('evaluacion_doc', models.IntegerField()),
                ('horario_atencion', models.DateTimeField()),
                ('disponibilidad', models.BooleanField()),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=20)),
                ('edad_paciente', models.IntegerField()),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='Ficha_Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=40)),
                ('prevision', models.CharField(max_length=15)),
                ('horario', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paciente')),
            ],
            options={
                'db_table': 'ficha_paciente',
            },
        ),
    ]
