# Generated by Django 5.0.7 on 2024-10-31 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_shopuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='email',
            field=models.EmailField(default=0, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
