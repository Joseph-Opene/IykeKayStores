# Generated by Django 3.1.7 on 2021-04-07 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0002_auto_20210406_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('decription', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
