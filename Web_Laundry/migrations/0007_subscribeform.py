# Generated by Django 3.1.2 on 2020-10-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Laundry', '0006_delete_subscribtionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.EmailField(max_length=254)),
            ],
        ),
    ]
