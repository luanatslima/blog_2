from django import forms
from django.core.exceptions import ValidationError
from .models import Mensagem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'email', 'telefone', 'cidade', 'mensagem']

    def clean_cidade(self):
        data = self.cleaned_data["cidade"]
        cidades_validas = ["SPP", "São Pedro", "Bom Jesus"]

        if (not data in cidades_validas):
            raise ValidationError("Não aceitamos a sua cidade.")
        
        return data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-md-6'),
                Column('email', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('telefone', css_class='col-md-6'),
                Column('cidade', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('mensagem', css_class='col-12'),
                css_class='row'
            ),
            Submit('submit', 'Enviar', css_class='btn btn-primary text-uppercase')
        )