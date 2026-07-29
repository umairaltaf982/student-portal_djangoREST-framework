from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from student_app.models import Student
from student_app.serializers import StudentSerializer

@csrf_exempt
def student_list(request):
    """
    List all students, or create a new student.
    """
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    """
    Retrieve, update or delete a student.
    """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        student.delete()
        return HttpResponse(status=204)





# 1. The @api_view decorator for working with function based views.
# 2. The APIView class for working with class-based views.
# e.g.

# @api_view(["GET", "POST"])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)