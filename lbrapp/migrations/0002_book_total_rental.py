# Generated by Django 4.2.1 on 2023-05-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbrapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
