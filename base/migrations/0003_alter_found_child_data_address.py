# Generated by Django 4.1 on 2022-12-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_found_child_data_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="found_child_data",
            name="address",
            field=models.CharField(max_length=100),
        ),
    ]
