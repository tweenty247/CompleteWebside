# Generated by Django 3.1.2 on 2020-10-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Laundry', '0003_formnames_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribtionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subscribe', models.EmailField(max_length=254)),
            ],
        ),
    ]
