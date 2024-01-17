import django_filters
from .models import *
from django.forms.widgets import TextInput

class jobfilter(django_filters.FilterSet):
    titre=django_filters.CharFilter(lookup_expr='icontains', label='',
                                    widget=TextInput(attrs={'placeholder': "Rechercher l'emploi qui vous convient",'class':'form-control'}))
    class Meta:
        model=job
        fields=['titre']

class jobfilteresp(django_filters.FilterSet):
    titre=django_filters.CharFilter(lookup_expr='icontains', label='',
                                    widget=TextInput(attrs={'placeholder': "Encuentra el trabajo que más te convenga",'class':'form-control'}))
    class Meta:
        model=job
        fields=['titre']