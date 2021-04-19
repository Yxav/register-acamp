from rest_framework import serializers
from peoples.models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id','first_name', 'last_name', 'phone', 'age',
                  'city', 'email', 'obs', 'food', 'sleep']
