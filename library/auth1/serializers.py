from rest_framework import serializers
from .models import Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = [
            'username', 'email',
        ]

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Admin
        fields = [
            'username', 'email', 'password',
        ]
        extra_kwargs = {
            'password':{
                'write_only' : True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        profile = Admin(**validated_data)
        profile.password = (password)
        profile.save()
        return profile