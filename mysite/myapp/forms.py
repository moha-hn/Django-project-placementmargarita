from django.forms import ModelForm
from .models import *
from django import forms
from django.core.validators import EmailValidator

class jobform(ModelForm):
    titre = forms.CharField(label='Titre', 
                    widget=forms.TextInput(attrs={'placeholder': 'Titre','class':'form-control'}))
    description = forms.CharField(label='Description', 
                    widget=forms.TextInput(attrs={'placeholder': 'Description','class':'form-control'}))
    employeur = forms.CharField(label='Employeur', 
                    widget=forms.TextInput(attrs={'placeholder': 'Employeur','class':'form-control'}))
    horaire = forms.CharField(label='Horaire', 
                    widget=forms.TextInput(attrs={'placeholder': ' (12h-18h)','class':'form-control'}))
    prix = forms.CharField(label='Salaire', 
                    widget=forms.TextInput(attrs={'placeholder': 'Salaire Par heure','class':'form-control'}))
    class Meta:
        
        model=job
        fields=['titre','description','prix','employeur','horaire']




class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Nom Complet'}))
    email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
   
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class ContactFormesp(forms.ModelForm):
    name = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))
    email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
   
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class candidatform(forms.ModelForm):
    nom = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    prenom = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Prenom'}))
    email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = candidat
        fields = ['nom', 'prenom', 'email','job', 'cv']

class candidatformesp(forms.ModelForm):
    nom = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    prenom = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'nombre de pila'}))
    email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = candidat
        fields = ['nom', 'prenom', 'email','job', 'cv']
        