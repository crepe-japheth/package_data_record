from .models import LocalPackage
from django import forms

EXCEPTION_CHOICES = (
    ('regular', 'regular'),
    ('exception', 'exception'),
)
class LocalPackageForm(forms.ModelForm):

    class Meta:
        model = LocalPackage
        fields = '__all__'
        # fields = ['sender_name', 'sender_email', 'sender_address', 'sender_phone_number', 'recipient_name', 'recipient_email', 'recipient_address', 'recipient_phone_number', 'package_type', 'package_destination', 'package_weight', 'tracking_number', 'branch', 'is_exception', 'content']
        widgets = {
            'sender_name':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress',
            }),
            'sender_email':forms.EmailInput(attrs={
                'class':'form-control',
                'id':'inputEmail4',
                'placeholder':'Email'
            }),
            'sender_address':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress',
            }),
            'sender_phone_number':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress',
                'placeholder':'07833......'
            }),
            'recipient_name':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
            'recipient_email':forms.EmailInput(attrs={
                'class':'form-control',
                'id':'inputAddress',
                'placeholder':'Email'
            }),
            'recipient_address':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
            'recipient_phone_number':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress',
                'placeholder':'+1 7625....'
            }),
            'package_type':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
            'package_destination':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
            'package_weight':forms.NumberInput(attrs={
                'class':'form-control',
                'id':'inputAddress',
                'placeholder':'weight in kilograms'
            }),
            'tracking_number':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
            'branch':forms.TextInput(attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
            'is_exception':forms.Select(choices=EXCEPTION_CHOICES, attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
            'content':forms.Textarea(attrs={
                'class':'form-control',
                'id':'inputAddress'
            }),
        }
        