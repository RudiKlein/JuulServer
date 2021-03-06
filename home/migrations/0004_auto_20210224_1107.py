# Generated by Django 3.1.6 on 2021-02-24 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210223_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deelnemers',
            old_name='emailadres_p',
            new_name='emailadres',
        ),
        migrations.RemoveField(
            model_name='deelnemers',
            name='emailadres_a',
        ),
        migrations.RemoveField(
            model_name='deelnemers',
            name='emailadres_s',
        ),
        migrations.AlterField(
            model_name='activiteiten',
            name='emailadres',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.persoonsgegevens'),
        ),
        migrations.AlterField(
            model_name='scorekaart',
            name='emailadres',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.persoonsgegevens'),
        ),
    ]
