from django.db import models


class PersoonsGegevens(models.Model):
    emailadres = models.CharField(max_length=45, default='')
    voornaam = models.CharField(max_length=45, default='')
    achternaam = models.CharField(max_length=45, default='')
    # optional = models.CharField(max_length=45, default='')
    gewicht = models.IntegerField(default=1)
    leeftijd = models.IntegerField(default=1)
    lengte = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Persoonsgegevens'
        verbose_name_plural = 'Persoonsgegevens'

    def __str__(self):
        # zet de naam van de entry als blok
        return self.emailadres


class Activiteiten(models.Model):
    activiteit = models.CharField(max_length=45, default='')
    eenheid = models.CharField(max_length=45, default='')
    # optional = models.CharField(max_length=45, default='')
    multiplier = models.FloatField(default=1)
    punten = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Activiteiten'
        verbose_name_plural = 'Activiteiten'

    def __str__(self):
        # zet de naam van de entry als blok
        return self.activiteit


class Doelstellingen(models.Model):
    activiteiten = models.ForeignKey(Activiteiten, on_delete=models.CASCADE, default=0)
    persoonsgegevens = models.ForeignKey(PersoonsGegevens, on_delete=models.CASCADE, default=0)
    # optional = models.CharField(max_length=45, default='')
    doelstelling = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Doelstellingen'
        verbose_name_plural = 'Doelstellingen'

    def __str__(self):
        # zet de naam van de entry als blok
        return self.persoonsgegevens.voornaam + ": " + self.activiteiten.activiteit + " " + str(self.doelstellingen) + "x"


class Scorekaart(models.Model):
    persoonsgegevens = models.ForeignKey(PersoonsGegevens, on_delete=models.CASCADE, default=0)
    activiteiten = models.ForeignKey(Activiteiten, on_delete=models.CASCADE, default=0)
    # optional = models.CharField(max_length=45, default='')
    jaar = models.IntegerField(default=1)
    maand = models.IntegerField(default=1)
    week = models.IntegerField(default=1)
    dag = models.IntegerField(default=1)
    duur = models.IntegerField(default=1)
    start_tijd = models.DateTimeField(default=0)
    eind_tijd = models.DateTimeField(default=0)

    class Meta:
        verbose_name = 'Scorekaart'
        verbose_name_plural = 'Scorekaart'

    def __str__(self):
        # zet de naam van de entry als blok
        return self.persoonsgegevens.voornaam + ": " + self.activiteiten.activiteit
