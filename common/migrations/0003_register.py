# Generated by Django 2.2.2 on 2019-06-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20190626_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('mark', models.IntegerField(default=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
