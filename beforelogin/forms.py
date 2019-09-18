from django import forms
import datetime
from django.contrib.auth.hashers import make_password, check_password


now = datetime.datetime.now()
c_choices=(
    ("IN", ("India")),
    ("MY", ("Malaysia")),
    ("SG", ("Singapore")))
g_choices=(("Male","Male"),("Female","Female"),("Other","Other"))
m_choices=(("January","January"),("February","February"),("March","March"),("April","April"),("May","May"),("June","June"),
           ("July", "July"), ("August", "August"), ("September", "September"),("October","October"),("November","November"),
           ("December","December"))

class Loginform(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'style': 'width:283px'}))
    Pwd = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width:283px'}))
    #def checked_in(self):


class Registerform(forms.Form):
    Name1 = forms.CharField(widget=forms.TextInput(attrs={'style': 'width:136px'}))
    Name2= forms.CharField(widget=forms.TextInput(attrs={'style': 'width:136px'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'style': 'width:274px'}))
    Create_Password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width:274px'}))
    Confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width:274px'}))
    Date_of_YEAR = forms.IntegerField(max_value=now.year,min_value=1900,widget=forms.NumberInput({'style': 'width:88px'}))
    Date_of_month=forms.ChoiceField(choices =m_choices,widget=forms.Select({'style': 'width:88px'}))
    Date_of_day=forms.IntegerField(max_value=31,min_value=1,widget=forms.NumberInput({'style': 'width:88px'}))
    Gender = forms.ChoiceField(choices =g_choices,widget=forms.Select({'style': 'width:274px'}))
    Mobile_phone = forms.CharField(widget=forms.TextInput(attrs={'style': 'width:274px'}))
    Location = forms.ChoiceField(choices =c_choices,widget=forms.Select(attrs={'style': 'width:274px'}))
    def clean(self):
        # cleaned_data = super(Registerform, self).clean()
        # print cleaned_data
        password1 = self.cleaned_data.get('Create_Password')
        password2 = self.cleaned_data.get('Confirm_Password')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        else:
            password1=make_password(password1)




class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

