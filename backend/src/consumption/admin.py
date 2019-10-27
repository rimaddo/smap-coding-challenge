from django.contrib import admin

from consumption.models import Area, Consumption, Tariff, User

MODELS = [
    Area,
    Consumption,
    Tariff,
    User,
]

for model in MODELS:
    admin.site.register(model)
