# Generated by Django 4.2.1 on 2023-09-13 01:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dataAC", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataac",
            name="conectionCode",
            field=models.CharField(max_length=10),
        ),
    ]