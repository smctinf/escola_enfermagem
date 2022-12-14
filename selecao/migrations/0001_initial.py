# Generated by Django 3.2.15 on 2022-10-17 19:08

from django.db import migrations, models
import django.db.models.deletion
import selecao.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90)),
                ('mes', models.CharField(choices=[('JAN', 'Janeiro'), ('FEV', 'Fevereiro'), ('MAR', 'Março'), ('ABR', 'Abril'), ('MAI', 'Maio'), ('JUN', 'Junho'), ('JUL', 'Julho'), ('AGO', 'Agosto'), ('SET', 'Setembro'), ('OUT', 'Outubro'), ('NOV', 'Novembro'), ('DEZ', 'Dezembro')], max_length=3)),
                ('ano', models.CharField(max_length=4)),
                ('dt_inicio_inscricao', models.DateField()),
                ('dt_final_inscricao', models.DateField()),
                ('dt_prova', models.DateField()),
                ('dt_resultado', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Horário',
                'verbose_name_plural': 'Horários',
                'ordering': ['local', 'horario'],
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(max_length=5)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.horario')),
            ],
            options={
                'ordering': ['horario', 'sala'],
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('rua', models.CharField(max_length=60)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('edital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='selecao.edital')),
            ],
            options={
                'verbose_name_plural': 'Locais',
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='horario',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.local'),
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90)),
                ('link', models.URLField()),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selecao.edital')),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('dt_nascimento', models.DateField(verbose_name='Data Nascimento')),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[selecao.functions.validate_CPF])),
                ('celular', models.CharField(max_length=11)),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(max_length=120)),
                ('deficiencia', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('qual_deficiencia', models.CharField(max_length=600)),
                ('necessidade', models.CharField(max_length=600)),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('chave', models.CharField(max_length=36, unique=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('edital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='selecao.edital')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Alocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.candidato')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.sala')),
            ],
            options={
                'verbose_name': 'Alocação',
                'verbose_name_plural': 'Alocações',
                'ordering': ['sala', 'candidato'],
            },
        ),
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.candidato')),
            ],
            options={
                'ordering': ['dt_inclusao'],
            },
        ),
    ]
