# Generated by Django 3.0.9 on 2020-08-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articlepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='author',
            field=models.CharField(default='NULL', max_length=250),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='intro_image',
            field=models.FileField(default='NULL', upload_to=''),
        ),
    ]
