from django import forms
from .models import NoinfoDetail

class DetailForm(forms.ModelForm):
    class Meta:
        model = NoinfoDetail
        fields = ['theme', 'name', 'type', 'form', 'tag', 'dim', 'episodes', 'duration', 'episode_start', 'episode_end', 'date_start', 'date_end', 'date_watch_start', 'date_watch_end', 'company', 'area']