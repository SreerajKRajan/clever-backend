from rest_framework import viewsets
from .models import (
    Therapist,
    Service,
    Location,
    ServiceAddon,
    CommissionRule,
    CommissionEntry,
)
from .serializers import (
    TherapistSerializer,
    ServiceSerializer,
    LocationSerializer,
    ServiceAddonSerializer,
    CommissionRuleSerializer,
    CommissionEntrySerializer,
)


class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ServiceAddonViewSet(viewsets.ModelViewSet):
    queryset = ServiceAddon.objects.all()
    serializer_class = ServiceAddonSerializer


class CommissionRuleViewSet(viewsets.ModelViewSet):
    queryset = CommissionRule.objects.all()
    serializer_class = CommissionRuleSerializer


class CommissionEntryViewSet(viewsets.ModelViewSet):
    queryset = CommissionEntry.objects.all()
    serializer_class = CommissionEntrySerializer
