# Generated by Django 3.0.9 on 2020-10-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0018_persondetectionpage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturedetectionpage',
            name='classification',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
