# Generated by Django 3.0.3 on 2020-04-05 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_textbody'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbody',
            name='index_key',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
