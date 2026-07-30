from student_app.models import Student
from student_app.serializers import StudentSerializer
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
from student_app.serializers import UserSerializer

"""
List all students, or create a new student.
"""

class StudentList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""
    Retrieve, update or delete a student instance.
"""
class StudentDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# Or if we want to make our code more generic
# Using the mixin classes we've rewritten the views to use slightly less code than before, 
# but we can go one step further. REST framework provides a set of already mixed-in generic views 
# that we can use to trim down our views.py module even more.

"""
from student_app.models import Student
from student_app.serializers import StudentSerializer
from rest_framework import generics


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
"""



# added for the authentication and permissions
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer