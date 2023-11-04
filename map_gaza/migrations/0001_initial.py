# Generated by Django 4.1.7 on 2023-11-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('date', models.DateTimeField()),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
