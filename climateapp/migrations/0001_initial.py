# Generated by Django 3.0.3 on 2020-02-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
