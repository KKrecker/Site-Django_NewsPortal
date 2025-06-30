from django import forms
from django.forms import ModelForm
from posts.models import Advertisement
from phonenumber_field.formfields import PhoneNumberField
from posts.models import Offer


class AdvertisementForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class":"green",
        "placeholder": 'Название'
    }))
    content = forms.CharField(widget=forms.TextInput(attrs={
        "class":"green",
        "placeholder": 'Контент'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        "class":"green",
        "placeholder":'Описание'
    }))
    class Meta:
        model = Advertisement
        fields = ["title", "content", "description"]



class OfferForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class":"green",
        "placeholder": ''
    }))
    content = forms.CharField(widget=forms.TextInput(attrs={
        "class":"green",
        "placeholder": 'Контент'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"green",
        "placeholder":'xxxxx@mail.ru'
    }))
    phone = PhoneNumberField(region = 'RU', widget=forms.TextInput(attrs={
        "class":"green",
        "placeholder":'+7xxxxxxxxx'
    }))

    class Meta:
        model = Offer
        fields = ["title", "content", "email","phone"]