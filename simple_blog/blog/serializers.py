from django.contrib.auth import get_user_model
from django.db.models import fields
from django.db.models.fields import NullBooleanField

from rest_framework import serializers

from .models import Blog

User = get_user_model


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    created = serializers.DateTimeField()
    # created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'