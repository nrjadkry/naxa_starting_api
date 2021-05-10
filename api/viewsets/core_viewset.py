from rest_framework import viewsets
from core.models import Student
from api.serializers.core_serializer import StudentSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework import status
from rest_framework.views import APIView

# Viewsets 
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.get_student_range(101,104)
	serializer_class = StudentSerializer

class StudentViewSet1(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# APIView
class StudentAPI(APIView):
    def get(self,request, pk=None, format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

    def put(self,request, pk, format=None):
        id=pk

        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request, pk ,format=None):
        id=pk

        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted'})

# Generic APIView
