# Generated by Django 4.0 on 2021-12-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_handling', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Payed', 'Payed'), ('NotPayed', 'NotPayed')], default='NotPayed', max_length=11),
        ),
    ]
