
from django import forms

from game_app.accounts.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('username', 'age', 'password')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"
