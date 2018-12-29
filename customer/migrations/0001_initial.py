# Generated by Django 2.1.3 on 2018-12-17 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('address', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('orders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
