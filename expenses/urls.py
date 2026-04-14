from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:expense_id>/remove/', views.remove_expense, name='remove_expense'),
    path('add/', views.add_expense, name='add_expense'),
    path('list/', views.list_expenses, name='list_expenses'),
    path('filter/', views.filter_expenses, name='filter_expenses'),
]
