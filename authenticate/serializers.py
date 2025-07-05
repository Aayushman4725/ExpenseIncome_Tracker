from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only = True, required = True)
    
    class Meta:
        model = User
        fields = ['username', 'password','confirm_password']
        
    
    def validate(self,attrs):
        if attrs['password']!=attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Passwords do not match with confirm password'})
        return attrs
    
    def create(self,validated_data):
        validated_data.pop('confirm_password')
        
        user = User.objects.create(username = validated_data['username'], password = validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    
    def validate(self,attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if not username or not password:
            raise serializers.ValidationError({'error': 'Both username and password fields are required to be filled'})
        
        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError({'error': 'Invalid Credentials'})
        
        attrs['user']=user
        
        return attrs
    
