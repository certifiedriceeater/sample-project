# Generated by Django 4.1.7 on 2023-04-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = Truefro

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=20)),
            ],
        ),
    ]