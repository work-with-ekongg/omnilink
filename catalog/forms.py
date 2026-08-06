from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vendor, Product

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply clean Tailwind classes to every form field automatically
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-2 border border-slate-200 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:outline-none text-sm'


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['business_name', 'whatsapp_number', 'bio', 'profile_image']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-200 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:outline-none text-sm'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-200 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:outline-none text-sm'}),
            'bio': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-200 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:outline-none text-sm', 'rows': 3}),
            'profile_image': forms.FileInput(attrs={'class': 'w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-semibold file:bg-emerald-50 file:text-emerald-700 hover:file:bg-emerald-100'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-200 rounded-xl focus:ring-emerald-500 focus:outline-none text-sm', 'placeholder': 'e.g. Nike Air Force 1'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-slate-200 rounded-xl focus:ring-emerald-500 focus:outline-none text-sm', 'placeholder': 'e.g. 15000'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-200 rounded-xl focus:ring-emerald-500 focus:outline-none text-sm', 'placeholder': 'Describe your product...'}),
            'image': forms.FileInput(attrs={'class': 'w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-semibold file:bg-emerald-50 file:text-emerald-700 hover:file:bg-emerald-100'})
        }