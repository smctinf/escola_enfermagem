# Generated by Django 3.2.15 on 2022-10-23 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0007_auto_20221019_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='alocacao',
            name='edital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='selecao.edital'),
        ),
        migrations.AddField(
            model_name='sala',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='selecao.local'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='autodeclaracao',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='O candidato é autodeclarado preto, pardo ou indígena'),
        ),
    ]