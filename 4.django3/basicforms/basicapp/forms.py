from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() !='z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH A Z")
class FormName(forms.Form):
    #name = forms.CharField(validators = [check_for_z], max_length=128)
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    verify_email = forms.EmailField(label = 'Enter your email again')
    #botcatcher = forms.CharField(validators= [validators.MaxLengthValidator(0)],required=False, widget=forms.HiddenInput)
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
    # custom clean method

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")
