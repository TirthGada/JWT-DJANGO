from rest_framework import serializers
from . models import MyUser
class MyUserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password', 'write_only': True})
    password2 = serializers.CharField(max_length=128)
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')
        extra_kwargs = {
            'password2': {'write_only': True},
        }

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if not password1:
            raise serializers.ValidationError('Password1 cannot be empty.')
        if password1 != password2:
            raise serializers.ValidationError('Both passwords do not match!')
        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user


class MyUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password', 'write_only': True})
    class Meta:
        model =MyUser
        fields=('email','password')