# Generated by Django 5.0.3 on 2024-04-12 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_deck_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vestibular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Correcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlCorrecao', models.URLField()),
                ('prova', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.prova')),
            ],
        ),
        migrations.CreateModel(
            name='Caderno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('urlProva', models.URLField()),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.prova')),
            ],
        ),
        migrations.AddField(
            model_name='prova',
            name='vestibular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vestibular'),
        ),
    ]
