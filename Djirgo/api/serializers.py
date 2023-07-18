from rest_framework import serializers

from task.models import Task, User
import datetime


class TaskSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Task
        #fields = ('text', 'pub_date',) #тут проблема с полями , 'age'
        fields = '__all__'
        #read_only_fields = ('owner',)

    def get_age(self, obj):
        age = obj.update_date - obj.pub_date
        total_seconds = age.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        formatted_age = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        return formatted_age


class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = User
        fields = '__all__' #('id', 'username',)
        #ref_name = 'ReadOnlyUsers'