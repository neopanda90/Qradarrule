# Generated by Django 3.0.8 on 2020-08-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qradar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_source', models.CharField(max_length=50)),
                ('name', models.TextField()),
                ('condition', models.TextField()),
                ('tactics', models.CharField(max_length=100)),
            ],
        ),
    ]