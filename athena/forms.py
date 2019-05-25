from django import forms

from .models import AthenaCard, AthenaRank

class AthenaCardCreateForm(forms.ModelForm):
    class Meta:
        model = AthenaCard
        fields = [
            'name',
            'roots',
            'dob',
            'incomplete',
            'face',
            'body',
            'bazooka',
            'tushy',
            'status',
            'mugshot',
            'images',
            'vid',
            'vid1',
            'vid2',
            'vid3',
            'vid4'
        ]
        labels = {
            'dob': ('Date of Birth ')
        }
        widgets = {
            'dob': forms.TextInput(attrs={'placeholder': ' mm/dd/yy e.g 03/31/85'}),
            'images': forms.ClearableFileInput(attrs={'multiple': True}),
            'vid': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class AthenaCardUpdateForm(forms.ModelForm):
    class Meta:
        model = AthenaCard
        fields = [
            'name',
            'details',
            'roots',
            'dob',
            'incomplete',
            'status',
            'mugshot',
            'images',
            'vid',
            'vid1',
            'vid2',
            'vid3',
            'vid4'
        ]
        labels = {
            'dob': ('Date of Birth ')
        }
        widgets = {
            'dob': forms.TextInput(attrs={'placeholder': ' mm/dd/yy e.g 03/31/85'}),
            'images': forms.ClearableFileInput(attrs={'multiple': True}),
            'vid': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class AthenaRankCreateForm(forms.ModelForm):
    class Meta:
        model = AthenaRank
        fields = [
            'athena',
            'rank'
        ]
        widgets ={
            'rank': forms.TextInput(attrs={'placeholder': AthenaRank.objects.latest('id').rank}),
        }

class AthenaRankUpdateForm(forms.ModelForm):
    class Meta:
        model = AthenaRank
        fields = [
            'athena',
            'rank'
        ]
