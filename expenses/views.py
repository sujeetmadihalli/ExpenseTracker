from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Q, Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime

@login_required
def dashboard(request):
    user = request.user
    today = timezone.now().date()
    first_day_of_month = today.replace(day=1)
    
    # Summary Statistics
    total_spent = Expense.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum'] or 0
    spent_this_month = Expense.objects.filter(user=user, date__gte=first_day_of_month).aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Data for Category Chart
    category_data = Expense.objects.filter(user=user).values('category').annotate(total=Sum('amount')).order_by('-total')
    
    # Data for Monthly Trend (last 6 months)
    six_months_ago = today - datetime.timedelta(days=180)
    monthly_trend = Expense.objects.filter(user=user, date__gte=six_months_ago).values('date').annotate(total=Sum('amount')).order_by('date')

    context = {
        'total_spent': total_spent,
        'spent_this_month': spent_this_month,
        'category_data': category_data,
        'monthly_trend': monthly_trend,
    }
    return render(request, 'expenses/dashboard.html', context)

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'expenses/register.html', {'form': form})

@login_required
def home(request):
    return redirect('dashboard')

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required
def list_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses/list_expenses.html', {'expenses': expenses})

@login_required
def filter_expenses(request):
    category = request.GET.get('category', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    min_amount = request.GET.get('min_amount', '')
    max_amount = request.GET.get('max_amount', '')

    filters = Q(user=request.user)
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

@login_required
def remove_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('list_expenses')
    return render(request, 'expenses/remove_expense.html', {'expense': expense})