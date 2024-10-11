from rest_framework import serializers
from .models import Watchlist

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['id', 'title', 'description', 'release_date', 'added_on']


from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=False, allow_blank=True)  # Make email optional

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, data):
        """
        Check that the two password entries match.
        """
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        # Remove password_confirm since we don't need to store it
        validated_data.pop('password_confirm')

        # Create the user using Django's built-in create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  # Provide an empty string if no email
            password=validated_data['password']
        )
        return user
