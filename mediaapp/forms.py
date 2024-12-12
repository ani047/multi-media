from django import forms
from django.db import models
from mediaapp.models import MediaData
class MediaForm(forms.ModelForm):
    class Meta:
        model = MediaData
        fields = "__all__"