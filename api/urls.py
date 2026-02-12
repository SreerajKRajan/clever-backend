from rest_framework.routers import DefaultRouter
from .views import (
    TherapistViewSet,
    ServiceViewSet,
    LocationViewSet,
    ServiceAddonViewSet,
    CommissionRuleViewSet,
    CommissionEntryViewSet,
)

router = DefaultRouter()
router.register(r"therapists", TherapistViewSet)
router.register(r"services", ServiceViewSet)
router.register(r"locations", LocationViewSet)
router.register(r"service-addons", ServiceAddonViewSet)
router.register(r"commission-rules", CommissionRuleViewSet)
router.register(r"commission-entries", CommissionEntryViewSet)

urlpatterns = router.urls
