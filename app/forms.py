from django.forms import ModelForm
from app.models import produtos

# Create the form class.
class produtosForm(ModelForm):
    class Meta:
        model = produtos
        fields = ['modelo', 'marca', 'preco']