from rest_framework import viewsets

from task.models import Task, User
from .serializers import TaskSerializer, UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        # if serializer.instance.author != self.request.user or хочу либо ты либо NULL:
        #     raise PermissionDenied('Удаление чужого контента запрещено!')
        #super(TaskViewSet, self).perform_update(serializer)
        serializer.save(performer=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer