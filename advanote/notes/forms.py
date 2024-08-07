import django.forms

import notes.models


class NoteForm(django.forms.ModelForm):
    class Meta:
        model = notes.models.Note
        fields = ["title", "text", "tags"]
        widgets = {
            "title": django.forms.TextInput(
                attrs={"placeholder": "Title"},
            ),
            "text": django.forms.Textarea(
                attrs={"placeholder": "Text"},
            ),
        }


__all__ = ()
