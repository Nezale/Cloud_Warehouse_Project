# Generated by Django 2.1.4 on 2019-01-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
            ],
        ),
    ]
