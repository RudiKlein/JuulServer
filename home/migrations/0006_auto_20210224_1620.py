# Generated by Django 3.1.6 on 2021-02-24 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210224_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorekaart',
            name='activiteiten',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.activiteiten'),
        ),
        migrations.AddField(
            model_name='scorekaart',
            name='deelnemers',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.deelnemers'),
        ),
        migrations.AddField(
            model_name='scorekaart',
            name='persoonsgegevens',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.persoonsgegevens'),
        ),
    ]