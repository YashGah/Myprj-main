# Generated by Django 5.1 on 2024-09-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_client_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.CharField(max_length=100),
        ),
    ]
