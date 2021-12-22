from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Perfil
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

 
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'placeholder':'Usuario...','class':'form-control'})
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder':'Contraseña...','class':'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder':'Repita la contraseña...','class':'form-control'})

class CustomLoginForm(AuthenticationForm):
     def __init__(self, *args, **kwargs):
        super(CustomLoginForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'placeholder':'Usuario...','class':'form-control'})
        self.fields['password'].widget = PasswordInput(attrs={'placeholder':'Contraseña...','class':'form-control'})
        

class ProfileForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre','apellido','email','provincia','ciudad','direccion','celular']

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder':'Nombre de usuario...','class':'form-control', 'autocomplete':'off'}),
            'apellido': forms.TextInput(attrs={'placeholder':'Apellido...','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email...','class':'form-control'}),
            'provincia': forms.TextInput(attrs={'placeholder':'Provincia...','class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'placeholder':'Ciudad...','class':'form-control'}),
            'direccion': forms.TextInput(attrs={'placeholder':'Direccion...','class':'form-control'}),
            'celular': forms.TextInput(attrs={'placeholder':'Celular...','class':'form-control'}),
        }

    
