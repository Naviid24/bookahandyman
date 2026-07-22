from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:

        model = Job

        # At this stage, we only ask the customer
        # to explain the job and optionally upload a photo.
        fields = [
            "description",
            "photo",
        ]

        widgets = {

            # Main job description box.
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "For example: "
                        "The kitchen tap is leaking and "
                        "I need someone to fix it."
                    ),
                    "rows": 7,
                }
            ),

            # Optional job photo.
            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
