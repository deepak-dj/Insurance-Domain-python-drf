from django.shortcuts import render
from .models import *
from  rest_framework import viewsets
from  .serializers import *


class User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Policy(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class Claim(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer