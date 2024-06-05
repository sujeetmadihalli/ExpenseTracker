from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def my_protected_view(request):
    user = request.user
    expenses = Expense.objects.filter(user=user)
    return render(request, 'login.html', {'expenses': expenses})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'expenses/home.html')

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def list_expenses(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'expenses/list_expenses.html', {'expenses': expenses})

def filter_expenses(request):
    category = request.GET.get('category', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    min_amount = request.GET.get('min_amount', '')
    max_amount = request.GET.get('max_amount', '')

    filters = Q()
    if category:
        filters &= Q(category__icontains=category)
    if start_date:
        filters &= Q(date__gte=start_date)
    if end_date:
        filters &= Q(date__lte=end_date)
    if min_amount:
        filters &= Q(amount__gte=min_amount)
    if max_amount:
        filters &= Q(amount__lte=max_amount)

    expenses = Expense.objects.filter(filters).order_by('-date')
    return render(request, 'expenses/filter_expenses.html', {
        'expenses': expenses, 
        'category': category,
        'start_date': start_date,
        'end_date': end_date,
        'min_amount': min_amount,
        'max_amount': max_amount
    })

def remove_expense(request, expense_id):
    print(f"Attempting to remove expense with ID: {expense_id}")  # Debug print
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        print("POST request received")  # Debug print
        expense.delete()
        return redirect('list_expenses')
    return render(request, 'expenses/remove_expense.html', {'expense': expense})