# Generated by Django 3.2.4 on 2021-06-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_modela_modelb_modelsc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelb',
            name='modela_ptr',
        ),
        migrations.RemoveField(
            model_name='modelsc',
            name='modela_ptr',
        ),
        migrations.AlterField(
            model_name='dropbox',
            name='document',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='modelA',
        ),
        migrations.DeleteModel(
            name='modelB',
        ),
        migrations.DeleteModel(
            name='modelsC',
        ),
    ]
