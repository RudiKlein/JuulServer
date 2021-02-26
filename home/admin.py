from django.contrib import admin

# Register your models here.

from .models import Doelstellingen, PersoonsGegevens, Activiteiten, Scorekaart

admin.site.register(Doelstellingen)
admin.site.register(PersoonsGegevens)
admin.site.register(Activiteiten)
admin.site.register(Scorekaart)
