from django.forms import ModelForm ,TextInput
from downloadYt.models import Enter



class EntryForm(ModelForm):
    class Meta:
        model=Enter
        fields =('Input',)
        widgets={'Input': TextInput(attrs={'class':'input','placeholder':'Enter Link Url'})}