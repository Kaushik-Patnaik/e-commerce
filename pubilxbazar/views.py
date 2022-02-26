from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def account(request):
    return render(request,'account.html')
def service(request):
    return render(request,'service.html')
def shopdetail(request):
    return render(request,'shopdetail.html')
def shop(request):
    return render(request,'shop.html')
def wishlist(request):
    return render(request,'wishlist.html')