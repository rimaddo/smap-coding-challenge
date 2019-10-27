from django.db import models


class User(models.Model):
    """Represents a user who consumes energy within the model."""

    external_id = models.TextField(
        unique=True,
        help_text="The external ID of this object. Must be unique.",
    )
    area = models.ForeignKey("Area", on_delete=models.CASCADE, related_name="area")
    tariff = models.ForeignKey("Tariff", on_delete=models.CASCADE, related_name="tariff")


class Area(models.Model):
    """Represents a geographical area within which users belong."""

    name = models.CharField(max_length=255, unique=True)


class Tariff(models.Model):
    """Represents a tariff level at which energy is consumed."""

    name = models.CharField(max_length=255, unique=True)


class Consumption(models.Model):
    """Represents consumption of energy by a user at a moment in time."""

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    datetime = models.DateTimeField()
    amount = models.FloatField(default=0)
