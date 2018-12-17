# Generated by Django 2.1.4 on 2018-12-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HonoraryLifeMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('deceased', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('name', models.TextField()),
                ('deceased', models.BooleanField(default=False)),
            ],
        ),
    ]
