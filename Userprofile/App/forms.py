from django.contrib.auth.forms import forms


class Add_Stud(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    img = forms.ImageField()
    caption = forms.CharField(widget=forms.Textarea)
    dob = forms.DateField(widget=forms.SelectDateWidget)
    designation = forms.CharField()
