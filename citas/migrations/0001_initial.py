# Generated by Django 4.0.1 on 2022-01-30 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
                ('eslogan', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('foto', models.ImageField(upload_to='home')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_esp', models.CharField(max_length=50)),
                ('descrip', models.TextField(verbose_name='Descripción de Especialidad')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('presentacion', models.CharField(max_length=50)),
                ('volumen', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.consulta')),
                ('medicamento', models.ManyToManyField(to='citas.Medicamento')),
            ],
            options={
                'verbose_name': 'Tratamiento',
                'verbose_name_plural': 'Tratamientos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de Paciente')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido de Paciente')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Identificación')),
                ('direccion', models.TextField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=10, verbose_name='Numero de Telefono')),
                ('foto', models.FileField(upload_to='pacientes')),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de Paciente')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido de Paciente')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Identificación')),
                ('direccion', models.TextField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=10, verbose_name='Numero de Telefono')),
                ('foto', models.FileField(upload_to='pacientes')),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medico',
            },
        ),
        migrations.CreateModel(
            name='Especialidad_Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_laboral', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes')], help_text='Seleccione un dia', max_length=20, verbose_name='Dia Laboral')),
                ('horario', models.CharField(choices=[('8:h00 - 8h30', '8:h00 - 8h30'), ('8h30 - 9h00', '8h30 - 9h00'), ('9h00 - 10h00', '9h00 - 10h00')], help_text='Seleccione el horario', max_length=30, verbose_name='Horario de Atención')),
                ('id_especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.especialidad')),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.medico')),
            ],
            options={
                'unique_together': {('dia_laboral', 'horario')},
            },
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.paciente'),
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('motivo', models.CharField(choices=[('Consulta', 'Consulta'), ('Revisión de Exámenes', 'Revisión de Exámenes'), ('Otro', 'Otro')], max_length=20, verbose_name='Motivo de cita')),
                ('esp_medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.especialidad_medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'unique_together': {('esp_medic', 'fecha_cita')},
            },
        ),
    ]
