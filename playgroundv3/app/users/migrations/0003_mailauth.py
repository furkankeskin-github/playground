# Generated by Django 4.1.7 on 2023-02-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('temptoken', models.CharField(max_length=256, unique=True)),
                ('verifycode', models.CharField(max_length=6)),
                ('logintime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
