from rest_framework import serializers
from .models import PersonalTask

class PersonalTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalTask
        fields = ['u_id', 'title', 'status', 'assigned_to', 'created_at', 'updated_at']
        read_only_fields = ['u_id', 'created_at', 'assigned_to',]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['assigned_to'] = user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.assigned_to != user:
            raise serializers.ValidationError("You can only update your own tasks.")
        return super().update(instance, validated_data)
    