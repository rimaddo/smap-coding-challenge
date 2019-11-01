from django.db import models


class User(models.Model):
    """Represents a user who consumes energy within the model."""

    external_id = models.TextField(
        unique=True,
        help_text="The external ID of this object. Must be unique.",
    )
    area = models.ForeignKey("Area", on_delete=models.SET_NULL, related_name="area", null=True)
    tariff = models.ForeignKey("Tariff", on_delete=models.SET_NULL, related_name="tariff", null=True)

    def __str__(self) -> str:
        return f'User(' \
               f'{self.external_id},' \
               f'Area: {getattr(self.area, "name", None)},' \
               f'Tariff: {getattr(self.tariff, "name", None)})'


class Area(models.Model):
    """Represents a geographical area within which users belong."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'Area({self.name})'


class Tariff(models.Model):
    """Represents a tariff level at which energy is consumed."""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'Tariff({self.name})'


class Consumption(models.Model):
    """Represents consumption of energy by a user at a moment in time."""

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    datetime = models.DateTimeField()
    amount = models.FloatField(default=0)

    def __str__(self) -> str:
        return f'Consumption(User: {self.user.external_id}, datetime: {self.datetime})'
