from .models import Info, Category,Orders
from rest_framework import serializers

class UsersSerializers(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Info
        fields = '__all__'

    def create(self, validated_data):
        category_name = validated_data.pop('category')['name']
        category = Category.objects.get(name=category_name)
        validated_data['category'] = category
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # Обработка обновления поля category
        category_name = validated_data.pop('category', None)
        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
            instance.category = category
            instance.save()
        
        # Обновление остальных полей
        return super().update(instance, validated_data)


class usersbot(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

