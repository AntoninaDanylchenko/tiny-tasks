from django import forms
from django.utils import timezone

from todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"},
            format="%Y-%m-%dT%H:%M"
        ),
        input_formats=["%Y-%m-%dT%H:%M"],
        label="Deadline",
        required=False,
    )

    class Meta:
        model = Task
        exclude = ["user"]

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")

        if deadline and deadline < timezone.now():
            raise forms.ValidationError("Deadline cannot be in the past.")

        return deadline


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ["user"]