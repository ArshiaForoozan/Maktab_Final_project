# Generated by Django 4.0 on 2021-12-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
