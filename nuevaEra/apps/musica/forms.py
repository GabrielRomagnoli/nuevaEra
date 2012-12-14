from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from musica.models import Comentario
from django.forms.widgets import Textarea

class ComentarioForm(forms.Form):
    contenido = forms.CharField(required=True, 
                                help_text=_("Maximo 500 caracteres"),
                                label=_("Comentario"),
                                 widget=forms.Textarea(attrs={'cols': 100, 'rows': 15}))
    
    class Meta:
        model = Comentario
        fields = ('contenido')
        
    def save(self, theme, user):
        comentario = Comentario(
                                contenido = self.cleaned_data['contenido'],
                                usuario = user,
                                tema = theme
                                )
        comentario.save()