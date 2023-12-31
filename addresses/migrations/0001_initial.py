# Generated by Django 3.2.9 on 2023-08-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('prefix_id', models.IntegerField(blank=True, null=True)),
                ('district_id', models.IntegerField(blank=True, null=True)),
                ('house', models.TextField(blank=True, null=True)),
                ('corpus', models.TextField(blank=True, null=True)),
                ('liter', models.TextField(blank=True, null=True)),
                ('villa', models.TextField(blank=True, null=True)),
                ('parcel', models.TextField(blank=True, null=True)),
                ('full_address', models.TextField(blank=True, null=True)),
                ('is_updated', models.BooleanField(blank=True, null=True)),
                ('is_actual', models.BooleanField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('municipality_id', models.FloatField(blank=True, null=True)),
                ('short_address', models.TextField(blank=True, null=True)),
                ('post_prefix', models.TextField(blank=True, null=True)),
                ('build_number', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'buildings',
                'managed': False,
            },
        ),
    ]
