from django import forms
from converter.utils import get_source_list

class StructuredDataForm( forms.Form ):
    source = forms.TypedChoiceField()
    database = forms.TypedChoiceField(choices = ())
    table = forms.TypedChoiceField(choices = ())
    query = forms.CharField(widget=forms.Textarea)
    response = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(StructuredDataForm, self).__init__(*args, **kwargs)
        self.fields['source'].choices = get_source_list()
