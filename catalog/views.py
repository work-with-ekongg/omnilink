from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import Vendor, Product
from .forms import CustomUserCreationForm, VendorForm, ProductForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'catalog/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'catalog/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

def home_view(request):
    return render(request, 'catalog/index.html')


@login_required(login_url='login')
def dashboard_view(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES, instance=vendor)
        if form.is_valid():
            vendor_profile = form.save(commit=False)
            vendor_profile.user = request.user
            vendor_profile.save()
            return redirect('dashboard')
    else:
        form = VendorForm(instance=vendor)
    
    context = {
        'form':form,
        'vendor':vendor
    }

    return render(request, 'catalog/dashboard.html', context)

def vendor_store_view(request, slug):
    vendor =  get_object_or_404(Vendor, slug=slug)
    products = vendor.products.filter(is_available=True)
    context = {
        'vendor':vendor,
        'products':products
    }
    return render(request, 'catalog/store.html', context)

@login_required(login_url='login')
def add_product_view(request):
    vendor =  Vendor.objects.filter(user=request.user).first()

    if not vendor:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product =form.save(commit=False)
            product.vendor = vendor
            product.save()
            return redirect('dashboard')
    else:
        form = ProductForm()

    return render(request, 'catalog/add.html',{'form':form})

@login_required(login_url='login')
def delete_product_view(request, pk):
    vendor = Vendor.objects.filter(user=request.user).first()
    product =Product.objects.filter(pk=pk, vendor=vendor).first()

    if product:
        product.delete()
    
    return redirect('dashboard')