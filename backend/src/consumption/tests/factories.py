import factory.fuzzy

from consumption.models import Area, Consumption, Tariff, User


class AreaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Area

    name = factory.Sequence(lambda i: f"Area-{i}")


class TariffFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tariff

    name = factory.Sequence(lambda i: f"Tariff-{i}")


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda i: f"User-{i}")
    area = factory.SubFactory(AreaFactory)
    tariff = factory.SubFactory(TariffFactory)


class ConsumptionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Consumption

    user = factory.SubFactory(UserFactory)
    datetime = factory.fuzzy.FuzzyNaiveDateTime()
    amount = factory.fuzzy.FuzzyFloat(low=0)
