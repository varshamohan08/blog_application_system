from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

    def validate(self, data):
        email = data.get('email')
        instance = self.instance

        if User.objects.exclude(pk=instance.pk if instance else None).filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")

        return data