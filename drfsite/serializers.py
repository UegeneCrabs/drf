from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.Serializer):
    task_type = serializers.CharField(max_length=20)
    task_name = serializers.CharField()
    task_description = serializers.CharField()
    task_members = serializers.CharField()
    date_creation = serializers.DateTimeField()
    days_to_complete = serializers.IntegerField()
    store = serializers.IntegerField(source='store.id')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task_type = validated_data.get('task_type', instance.task_type)
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.task_description = validated_data.get('task_description', instance.task_description)
        instance.task_members = validated_data.get('task_members', instance.task_members)
        instance.date_creation = validated_data.get('date_creation', instance.date_creation)
        instance.days_to_complete = validated_data.get('days_to_complete', instance.days_to_complete)
        instance.store_id = validated_data.get('store.id', instance.store_id)
        instance.save()
        return instance
