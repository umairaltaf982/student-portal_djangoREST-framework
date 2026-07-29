from django.urls import path
from student_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("students/", views.student_list),
    path("students/<int:pk>/", views.student_detail)
]

"""
urlpatterns = format_suffix_patterns(urlpatterns)
"""
# it is used when the user wants to change the request type. 
# for example: instead of json he want to use html request
# to apply this we also need to change our view methods to:
# def snippet_list(request, format=None): 
#     and 
# def snippet_detail(request, pk, format=None):