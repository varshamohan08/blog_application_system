# serializers.py
from rest_framework import serializers
from user_app.serializers import UserSerializer
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'publication_date', 'author', 'updated_date']
    
    def create(self, validated_data):
        # import pdb;pdb.set_trace()
        request = self.context.get('request')
        validated_data['author']=request.user
        note = Blog.objects.create(**validated_data)
        return note

    def update(self, instance, validated_data):
        request = self.context.get('request')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.updated_by = request.user
        instance.save()
        return instance