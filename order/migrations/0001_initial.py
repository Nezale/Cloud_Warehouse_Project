# Generated by Django 2.1.3 on 2018-12-08 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
        ('shiping_method', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='payment.Payment')),
                ('shipping_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shiping_method.ShippingMethod')),
            ],
        ),
    ]