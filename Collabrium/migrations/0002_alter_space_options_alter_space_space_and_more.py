# Generated by Django 5.0.6 on 2024-12-17 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collabrium', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='space',
            options={'verbose_name': 'Зона', 'verbose_name_plural': 'Зона'},
        ),
        migrations.AlterField(
            model_name='space',
            name='space',
            field=models.CharField(max_length=300, verbose_name='зона'),
        ),
        migrations.AlterField(
            model_name='space',
            name='space_en',
            field=models.CharField(max_length=300, null=True, verbose_name='зона'),
        ),
        migrations.AlterField(
            model_name='space',
            name='space_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='зона'),
        ),
        migrations.AlterField(
            model_name='space',
            name='space_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='зона'),
        ),
    ]
