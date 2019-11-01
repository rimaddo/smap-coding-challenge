from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from consumption.views import (
    AreaViewSet,
    ConsumptionViewSet,
    TariffViewSet,
    UserViewSet,
    number_of_users_by_area,
    user_consumption_by_time_of_day,
)

router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"areas", AreaViewSet)
router.register(r"tariffs", TariffViewSet)
router.register(r"consumptions", ConsumptionViewSet)

urlpatterns = [
    url(r"", include(router.urls)),
    url(r'^number_of_users_by_area/', number_of_users_by_area),
    url(r'^user_consumption_by_time_of_day/', user_consumption_by_time_of_day),
]
