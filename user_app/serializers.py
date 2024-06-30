from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

    def validate(self, data):
        email = data.get('email')
        instance = self.instance

        if User.objects.exclude(pk=instance.pk if instance else None).filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")

        return data
    
    def create(self, validated_data):
        import pdb;pdb.set_trace()
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
        instance.username = instance.email
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
        instance.username = instance.email
        instance.save()
        return instance
