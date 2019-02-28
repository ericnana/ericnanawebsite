from django import forms
from django.core.validators import validate_email


class ContactForm(forms.Form):
    #Email = forms.EmailField(required=True)
    #Subject = forms.CharField(required=True,max_length=100)
    #Message = forms.CharField(widget=forms.Textarea, required=True)
    #FirstName = forms.FirstNameField(required=False)
    #LastName = forms.LAstNameField(required=False)
    #Telephone = forms.TelephoneField(required=False)
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)
    #your_name = forms.CharField(label='Your name', max_length=100)

    
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    #content = forms.CharField(required=True,widget=forms.Textarea )
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={'cols': 3, 'rows': 5}))


    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name:"
        self.fields['contact_email'].label = "Email:"
        self.fields['content'].label = "Message:"
        self.fields['content'].widget.attrs['cols'] = 3
        self.fields['content'].widget.attrs['rows'] = 5
     



