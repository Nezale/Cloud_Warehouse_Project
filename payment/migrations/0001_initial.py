# Generated by Django 2.1.3 on 2018-12-08 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_method', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentAmount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paymentDate', models.DateTimeField(auto_now_add=True)),
                ('creditCardMember', models.CharField(max_length=50)),
                ('creditCardEXPCode', models.CharField(max_length=7)),
                ('cardHoldersName', models.CharField(max_length=30)),
                ('paymentMethod', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment_method.PaymentMethod')),
            ],
        ),
    ]
