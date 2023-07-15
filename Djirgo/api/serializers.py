from rest_framework import serializers

from task.models import Task
import datetime as dt


class TaskSerializer(serializers.ModelSerializer):
    #age = serializers.SerializerMethodField()
    #owner = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Task
        #fields = ('text', 'pub_date',) #тут проблема с полями , 'age'
        fields = '__all__'
        #read_only_fields = ('owner',)

    # def get_age(self, obj):
    #     return dt.datetime.now() - obj.pub_date

