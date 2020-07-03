from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bank, Branch
from .serializers import BranchSerializer

# Create your views here.
class DetailView(APIView):
    def get(self, request, ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(branch)
        return Response(serializer.data)


class ListView(APIView):
    def get(self, request, city, bank):
        branch_qset = Branch.objects.filter(
            city__iexact=city, bank__name__icontains=bank)
        serializer = BranchSerializer(branch_qset, many=True)
        return Response(serializer.data)
