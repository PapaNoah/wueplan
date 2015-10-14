from django import forms
from .models import Lines, Station

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset

class BusSelectionForm(forms.Form):
  station_choices = [(str(x),str(x)) for x in Station.objects.all()]
  lines_choices = [(str(x),str(x)) for x in Lines.objects.all()]
  
  lines_field = forms.ChoiceField(choices=lines_choices)
  station_field = forms.ChoiceField(choices=station_choices)
  
  def __init__(self, *args, **kwargs):
    super(BusSelectionForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
            'lines_field',
            'station_field',
            ButtonHolder(
                Submit('search', 'Suchen'))
    )