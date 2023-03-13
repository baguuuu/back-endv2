from rest_framework import serializers
from models import Configuration, Groupes, Users

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class GroupesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupes
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'