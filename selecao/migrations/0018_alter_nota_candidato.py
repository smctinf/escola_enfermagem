# Generated by Django 3.2.13 on 2022-11-03 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0017_alter_nota_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='selecao.candidato'),
        ),
    ]
