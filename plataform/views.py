from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pills

# Create your views here.
@login_required(login_url="/auth/login")
def home(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.getlist('category')

    # medicines = Pills.objects.all()
    if min_price or max_price or category:
        if not min_price:
            min_price = 0
        if not max_price:
            max_price = 99999999
        if not category:
            category = ['G','S']


        medicines = Pills.objects.filter(price__gte=min_price)\
        .filter(price__lte=max_price)\
        .filter(category__in=category)
    else:
        medicines = Pills.objects.all()
    return render(request, 'home.html', {'medicines': medicines})

def product(request, id):
    product = get_object_or_404(Pills, id=id)
    suggestions = Pills.objects.filter(category=product.category).exclude(id=id)[:2]
    return render(request, 'product.html', {'product': product, 'suggestions': suggestions})
