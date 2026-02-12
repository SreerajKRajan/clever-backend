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
    therapist_id = serializers.SerializerMethodField()
    service_id = serializers.SerializerMethodField()
    location_id = serializers.SerializerMethodField()
    
    class Meta:
        model = CommissionEntry
        fields = "__all__"
        extra_kwargs = {
            'therapist': {'write_only': True, 'required': False, 'allow_null': True},
            'service': {'write_only': True, 'required': False, 'allow_null': True},
            'location': {'write_only': True, 'required': False, 'allow_null': True},
        }
    
    def get_therapist_id(self, obj):
        return str(obj.therapist.id) if obj.therapist else None
    
    def get_service_id(self, obj):
        return str(obj.service.id) if obj.service else None
    
    def get_location_id(self, obj):
        return str(obj.location.id) if obj.location else None
    
    def to_internal_value(self, data):
        # Handle therapist_id, service_id, location_id from frontend
        # Create a copy to avoid modifying the original dict during iteration
        data = data.copy() if hasattr(data, 'copy') else dict(data)
        
        if 'therapist_id' in data:
            therapist_id = data.pop('therapist_id')
            if therapist_id:  # Only set if not None/empty
                data['therapist'] = therapist_id
        
        if 'service_id' in data:
            service_id = data.pop('service_id')
            if service_id:  # Only set if not None/empty
                data['service'] = service_id
        
        if 'location_id' in data:
            location_id = data.pop('location_id')
            if location_id:  # Only set if not None/empty
                data['location'] = location_id
        
        return super().to_internal_value(data)
