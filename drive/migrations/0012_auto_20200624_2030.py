# Generated by Django 3.0.7 on 2020-06-25 00:30

from django.db import migrations, models
import taggit.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('drive', '0011_auto_20200624_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='user',
            name='carpeta_raiz',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='fecha_upload',
            field=models.DateField(default='2020-06-25'),
        ),
        migrations.AlterField(
            model_name='carpeta',
            name='fecha_creacion',
            field=models.DateField(default='2020-06-25'),
        ),
        migrations.AlterField(
            model_name='carpeta',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(default='2020-06-25'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2020-06-25'),
        ),
    ]