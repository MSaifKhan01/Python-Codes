from rest_framework import serializers

from CrudApp.models import Student

from CrudApp.models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= '__all__'



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        