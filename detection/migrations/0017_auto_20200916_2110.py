# Generated by Django 3.0.9 on 2020-09-16 13:10

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('detection', '0016_flagdetectionindexpage_flagdetectionpage_flagdetectionpageresultimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='jointdetectionpage',
            name='gun_result',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.CreateModel(
            name='JointDetectionPageGunImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gun_images', to='detection.JointDetectionPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]