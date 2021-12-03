from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'        
        
#fields = ('firstname', 'lastname' and so on)
#we can also use __all__ in order to receive all the fields or datas