# Generated by Django 3.0.9 on 2020-08-11 14:14

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('article', '0003_auto_20200811_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='intro_image',
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='author',
            field=models.CharField(default='Admin', max_length=250),
        ),
        migrations.CreateModel(
            name='ArticlePageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='article.ArticlePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
