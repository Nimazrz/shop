# Generated by Django 5.0.7 on 2024-10-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_fix_duplicate_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]