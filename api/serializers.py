from rest_framework import serializers
from .models import (
    Therapist,
    Service,
    Location,
    ServiceAddon,
    CommissionRule,
    CommissionEntry,
)


class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ServiceAddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAddon
        fields = "__all__"


class CommissionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionRule
        fields = "__all__"


class CommissionEntrySerializer(serializers.ModelSerializer):
    therapist_id = serializers.UUIDField(source='therapist.id', read_only=True)
    service_id = serializers.UUIDField(source='service.id', read_only=True)
    location_id = serializers.UUIDField(source='location.id', read_only=True)
    
    class Meta:
        model = CommissionEntry
        fields = "__all__"
        extra_kwargs = {
            'therapist': {'write_only': True, 'required': False},
            'service': {'write_only': True, 'required': False},
            'location': {'write_only': True, 'required': False},
        }