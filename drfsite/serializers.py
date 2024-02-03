from rest_framework import serializers

from .models import Task, Store
import random


# class StoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = '__all__'
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'owner']


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task_type = serializers.CharField(max_length=20)
    task_name = serializers.CharField()
    task_description = serializers.CharField()
    task_members = serializers.CharField()
    date_creation = serializers.DateTimeField()
    days_to_complete = serializers.IntegerField()
    store = StoreSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.SerializerMethodField()  # Добавлено поле для имени пользователя

    def get_username(self, obj):
        return obj.user.username if obj.user else None

    def create(self, validated_data):
        store_data = validated_data.pop('store', {})
        store_name = store_data.get('name')
        store_owner = store_data.get('owner')

        store_token = ''.join(str(random.randint(0, 9)) for _ in range(8))

        store_instance, created = Store.objects.get_or_create(
            name=store_name,
            owner=store_owner,
            defaults={'token': store_token}
        )

        validated_data['store'] = store_instance
        task_instance = Task.objects.create(**validated_data)

        return task_instance

    def update(self, instance, validated_data):
        store_data = validated_data.pop('store', {})
        instance.store.name = store_data.get('name', instance.store.name)
        instance.store.owner = store_data.get('owner', instance.store.owner)
        instance.store.save()

        instance.task_type = validated_data.get('task_type', instance.task_type)
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.task_description = validated_data.get('task_description', instance.task_description)
        instance.task_members = validated_data.get('task_members', instance.task_members)
        instance.date_creation = validated_data.get('date_creation', instance.date_creation)
        instance.days_to_complete = validated_data.get('days_to_complete', instance.days_to_complete)
        instance.save()

        return instance
