from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to Restaurant Management System"})
    def homepage(request):
        return render(request, 'homepage.html')  # use exact file name

    




