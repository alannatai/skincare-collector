from django.forms import ModelForm
from .models import Progress

class ProgressForm(ModelForm):
  class Meta:
    model = Progress
    fields = ['date', 'status']