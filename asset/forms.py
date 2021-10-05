from django import forms
from django.contrib.auth.models import User

from .models import Asset

# from django.utils.translation import gettext_lazy as _

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'model', 'serial', 'user', 'purchaseDate', 'warranty', 'type', 'status', 'description']
        labels = {
            'user': 'Assigned to',
            'purchaseDate': 'Purchase Date',
            'warranty': 'Warrenty (in days)',
        }
        widgets = {
            'purchaseDate': forms.SelectDateWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        users = User.objects.all()
        self.fields['user'].choices = [(user.pk, user.get_full_name()) for user in users]
