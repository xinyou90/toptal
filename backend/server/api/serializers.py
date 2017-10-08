from rest_framework import serializers
from .models import Record, User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'role', 'expected_cal')

class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'role', 'expected_cal', 'password')
    extra_kwargs = { 'password': { 'write_only': True } }

  def create(self, validated_data):
    print(validated_data)
    user = super(UserCreateSerializer, self).create(validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user

class UserUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'role', 'expected_cal', 'password')
    extra_kwargs = { 'password': { 'write_only': True, 'required': False } }

  def update(self, instance, validated_data):
    user = super(UserUpdateSerializer, self).update(self.instance, validated_data)
    if 'password' in validated_data:
      user.set_password(validated_data['password'])
    user.save()
    return user

class RecordSerializer(serializers.ModelSerializer):
  class Meta:
    model = Record
    fields = '__all__'
