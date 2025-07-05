from django.contrib import admin
from django.urls import path,include
from .views import ExpenseIncomeView,ExpenseIncomeDetailView


urlpatterns = [
   path('expense-income/', ExpenseIncomeView.as_view(), name = 'expense-income'),
   path('expense-income-detail/<int:pk>/', ExpenseIncomeDetailView.as_view(), name = 'expense-income-detail')
]