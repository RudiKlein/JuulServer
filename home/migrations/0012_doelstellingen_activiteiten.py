# Generated by Django 3.1.6 on 2021-02-24 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210224_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='doelstellingen',
            name='activiteiten',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.activiteiten'),
        ),
    ]
