from rest_framework import serializers
from rest_framework.authtoken.models import Token
from herramientasweb_api.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

class ProfilesSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = "__all__"
class ProfilesAllSerializer(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = '__all__'
        depth = 1


# Serializers para Materia
class MateriaSerializer(serializers.ModelSerializer):
    nrc = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=True)

    class Meta:
        model = Materia
        fields = ('nrc','nombre')

class MateriasSerializer(serializers.ModelSerializer):
    materia=MateriaSerializer(read_only=True)
    class Meta:
        model = Materia
        fields = "__all__"

class MateriasAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
        depth = 1