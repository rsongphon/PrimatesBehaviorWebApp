# Generated by Django 5.0.7 on 2024-07-23 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimatesGameAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixationgameconfig',
            name='instance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fixationgameinstance', to='PrimatesGameAPI.gameinstances'),
        ),
        migrations.CreateModel(
            name='FixationGameReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='fixationreportgameinstance', to='PrimatesGameAPI.gameinstances')),
            ],
        ),
        migrations.CreateModel(
            name='FixationGameResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('feedback', models.BooleanField()),
                ('feedbacktype', models.CharField(max_length=10)),
                ('fixationreport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PrimatesGameAPI.fixationgamereport')),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportname', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PrimatesGameAPI.games')),
            ],
        ),
        migrations.AddField(
            model_name='fixationgamereport',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PrimatesGameAPI.reports'),
        ),
    ]
