# Generated by Django 4.1.7 on 2023-03-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividade', models.CharField(max_length=120)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
