# Generated by Django 4.2.1 on 2023-06-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postPicture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
