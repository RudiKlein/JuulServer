# Generated by Django 3.1.6 on 2021-02-24 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210224_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activiteiten',
            name='emailadres',
        ),
        migrations.RemoveField(
            model_name='deelnemers',
            name='emailadres',
        ),
        migrations.RemoveField(
            model_name='scorekaart',
            name='emailadres',
        ),
    ]