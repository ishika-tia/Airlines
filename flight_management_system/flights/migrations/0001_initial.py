# Generated by Django 4.1.3 on 2022-11-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dep_time', models.CharField(blank=True, max_length=5, null=True)),
                ('arr_time', models.CharField(blank=True, max_length=5, null=True)),
                ('service', models.CharField(blank=True, max_length=20, null=True)),
                ('aircraft_id', models.IntegerField(blank=True, null=True)),
                ('route_no', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'flight',
                'managed': False,
            },
        ),
    ]
