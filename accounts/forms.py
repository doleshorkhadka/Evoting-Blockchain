from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    first_name.widget.attrs.update({'class': 'form-control'})

    last_name = forms.CharField(max_length=100)
    last_name.widget.attrs.update({'class': 'form-control'})

    email = forms.EmailField()
    email.widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }
        help_texts = {
            "username":None,
        }
# overiding UserCreationForm to hide default help text  #
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].help_text=''
            self.fields['password2'].help_text=''


class register_form(forms.ModelForm):

    DISTRICT = (
        ("Sunsari","Sunsari"),
        ("Morang","Morang"),
        ("Jhapa","Jhapa"),
    )

    PROVIENCE = (
        ("1","Provience 1"),
        ("2","Provience 2"),
        ("3","Bagmati Provience"),
        ("4","Gandaki Provience"),
        ("5","Lumbini Provience"),
        ("6","Karnali Provience"),
        ("7","Sudurpaschim Provience"),
    )

    GENDER = (
        ("1","Male"),
        ("2","Female"),
        ("3","Others"),
    )

    district = forms.ChoiceField(choices = DISTRICT)
    district.widget.attrs.update({'class': 'form-control'})

    provience_number = forms.ChoiceField(choices = PROVIENCE)
    provience_number.widget.attrs.update({'class': 'form-control'})

    gender = forms.ChoiceField(choices = GENDER)
    gender.widget.attrs.update({'class': 'form-control'})

    dob_ad = forms.DateField()
    dob_ad.widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
    dob_ad.widget.attrs.update({'class': 'form-control'})

    dob_bs = forms.DateField()
    dob_bs.widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
    dob_bs.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Profile
        fields = ['docs_front','docs_back','user_image','father_name','grand_father_name','provience_number','district','phone_number','gender','dob_ad','dob_bs']
        widgets = {
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            'grand_father_name':forms.TextInput(attrs={'class':'form-control'}),
        }