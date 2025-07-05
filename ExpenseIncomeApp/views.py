from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer
from authenticate.permissions import *

# Create your views here.

class ExpenseIncomeView(ListCreateAPIView):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [IsUser]
   
   
    def get_queryset(self):
        return ExpenseIncome.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        
class ExpenseIncomeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [IsUser]
    
    
    def get_queryset(self):
        return ExpenseIncome.objects.filter(user = self.request.user)
        

       
