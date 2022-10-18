# Generated by Django 3.2.15 on 2022-10-17 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0002_edital_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloads',
            name='dt_inclusao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edital',
            name='dt_inclusao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]