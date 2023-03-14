# Generated by Django 3.0.9 on 2020-08-13 07:00

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectionPageResultImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_images', to='detection.DetectionPage')),
                ('result_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+++', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetectionPagePsenetImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='psenet_images', to='detection.DetectionPage')),
                ('psenet_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='++++', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]