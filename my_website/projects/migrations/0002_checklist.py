# Generated by Django 3.0.3 on 2020-03-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist_header', models.CharField(max_length=100)),
                ('checklist_entry', models.TextField()),
            ],
        ),
    ]
