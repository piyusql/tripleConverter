from django import forms
from converter.utils import get_source_list

class StructuredDataForm( forms.Form ):
    source = forms.TypedChoiceField()
    database = forms.TypedChoiceField(required = False)
    table = forms.TypedChoiceField(required = False)
    query = forms.CharField(widget=forms.Textarea, required = False)
    response = forms.CharField(widget=forms.Textarea, required = False)

    def __init__(self, *args, **kwargs):
        super(StructuredDataForm, self).__init__(*args, **kwargs)
        choices = [('','Please select Source')]
        choices.extend(get_source_list())
        self.fields['source'].choices = choices
