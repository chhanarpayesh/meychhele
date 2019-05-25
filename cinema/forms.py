from django import forms

from .models import CinemaBook, DesignShot, FoodShot, LocationShot, Beginnings, Endings
from django.utils.translation import gettext_lazy as _
from django.forms import inlineformset_factory

class CinemaBookCreateForm(forms.ModelForm):
    class Meta:
        model = CinemaBook
        fields = [
            'name',
            'language',
            'category',
            'year',
            'cinto',
            'dialogs',
            'popref',
            'public',
        ]
        labels = {
            'cinto': _('Amazing Camera Movements'),
            'popref': _('Pop Culture References made by characters.'),
        }

class CinemaBookUpdateForm(forms.ModelForm):
    class Meta:
        model = CinemaBook
        fields = [
            'language',
            'cinto',
            'dialogs',
            'popref',
            'metascore',
            'meter',
            'cast',
            'director',
            'synopsis',
            'public',
        ]
        labels = {
            'cinto': _('Amazing Camera Movements'),
            'popref': _('Pop Culture References made by characters.'),
        }

class DesignShotForm(forms.ModelForm):
    class Meta:
        model = DesignShot
        fields = ['cinema', 'dimage']
        labels = {
            'cinema':_('The Movie'),
            'dimage': _('Design Shot'),
        }

    def __init__(self, user=None, *args, **kwargs):
        super(DesignShotForm, self).__init__(*args, **kwargs)
        # only show cinemas created by user
        self.fields['cinema'].queryset = CinemaBook.objects.filter(owner=user).exclude(verify=False)

class FoodShotForm(forms.ModelForm):
    class Meta:
        model = FoodShot
        fields = ['cinema', 'fimage']
        labels = {
            'cinema':_('Pick A Movie'),
            'fimage': _('Food Shot'),
        }

    def __init__(self, user=None, *args, **kwargs):
        super(FoodShotForm, self).__init__(*args, **kwargs)
        # only show cinemas created by user
        self.fields['cinema'].queryset = CinemaBook.objects.filter(owner=user).exclude(verify=False)

class LocationShotForm(forms.ModelForm):
    class Meta:
        model = LocationShot
        fields = ['cinema', 'limage']
        labels = {
            'cinema':_('Pick A Movie'),
            'limage': _('Location Shot'),
        }

    def __init__(self, user=None, *args, **kwargs):
        super(LocationShotForm, self).__init__(*args, **kwargs)
        # only show cinemas created by user
        self.fields['cinema'].queryset = CinemaBook.objects.filter(owner=user).exclude(verify=False)

class BeginningsForm(forms.ModelForm):
    class Meta:
        model = Beginnings
        fields = ['cinema', 'scenes', 'lines']
        labels = {
            'cinema':_('Pick A Movie'),
            'lines': _('Opening Lines'),
            'scenes': _('Opening Scenes'),
        }

    def __init__(self, user=None, *args, **kwargs):
        super(BeginningsForm, self).__init__(*args, **kwargs)
        # only show cinemas created by user
        self.fields['cinema'].queryset = CinemaBook.objects.filter(owner=user).exclude(verify=False)


class EndingsForm(forms.ModelForm):
    class Meta:
        model = Endings
        fields = ['cinema', 'scenes', 'lines']
        labels = {
            'cinema':_('Pick A Movie'),
            'lines': _('Endings Lines'),
            'scenes': _('Endings Scenes'),
        }

    def __init__(self, user=None, *args, **kwargs):
        super(EndingsForm, self).__init__(*args, **kwargs)
        # only show cinemas created by user
        self.fields['cinema'].queryset = CinemaBook.objects.filter(owner=user).exclude(verify=False)
