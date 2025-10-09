from django import forms
from apps.galeria.models import Fotografia


class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descriçao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário '
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={'class':'forms-control'}),
            'legenda': forms.TextInput(attrs={'class':'forms-control'}),
            'categoria': forms.Select(attrs={'class':'forms-control'}),
            'descricao': forms.Textarea(attrs={'class':'forms-control'}),
            'foto': forms.FileInput(attrs={'class':'forms-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={'class':'forms-control',
                       'type':'date'}),
            'usuario': forms.Select(attrs={'class':'forms-control'})
        }
        