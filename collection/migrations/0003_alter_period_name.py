# Generated by Django 4.2.6 on 2023-10-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_alter_genre_name_alter_period_name_alter_style_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]