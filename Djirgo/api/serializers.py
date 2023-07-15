from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('text','pub_date') #тут проблема с полями
        #fields = '__all__'
