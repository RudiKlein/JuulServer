# Generated by Django 3.1.6 on 2021-02-27 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userentry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doelstellingen',
            name='activiteiten',
        ),
        migrations.RemoveField(
            model_name='doelstellingen',
            name='persoonsgegevens',
        ),
        migrations.RemoveField(
            model_name='scorekaart',
            name='activiteiten',
        ),
        migrations.RemoveField(
            model_name='scorekaart',
            name='persoonsgegevens',
        ),
        migrations.DeleteModel(
            name='Activiteiten',
        ),
        migrations.DeleteModel(
            name='Doelstellingen',
        ),
        migrations.DeleteModel(
            name='PersoonsGegevens',
        ),
        migrations.DeleteModel(
            name='Scorekaart',
        ),
    ]
