import re

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Text


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ["text"]

    def clean_text(self):
        text = self.cleaned_data["text"]
        if re.sub(r"[^\w\s]", "", text) == "":
            raise ValidationError(_("Input at least one word"))
        return text
