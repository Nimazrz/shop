# Generated by Django 5.0.7 on 2024-10-21 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_name_order_first_name_order_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='province',
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_address', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=10)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('order_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='orders.order')),
            ],
        ),
    ]
