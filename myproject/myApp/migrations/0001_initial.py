# Generated by Django 5.1.4 on 2025-01-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bk_name', models.CharField(max_length=100)),
                ('bk_number', models.IntegerField()),
            ],
        ),
    ]