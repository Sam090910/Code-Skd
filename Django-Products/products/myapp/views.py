from django.shortcuts import render

# Create your views here.

def homepage(request):
    from .models import Product
    products = Product.objects.all()
    ctr = 0
    prs = []
    for i in products:
        ctr += 1
        prs.append(i)
    pr = prs[1::]
    val = {"name": "Products-Display" ,"products": pr, "desc": "This Is The Best Website To Display Your Products", "First": prs[0]}
    print(prs[0].image)
    return render(request, 'myapp/index.html', val)