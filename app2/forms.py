from django import forms
from app.models import *
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class MainCategorieForm(forms.ModelForm):
    class Meta:
        model = MainCategorie
        fields = '__all__'

class SubCategorieForm(forms.ModelForm):
    class Meta:
        model = SubCategorie
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class HorizontalAdsForm(forms.ModelForm):
    class Meta:
        model = HorizontalAds
        fields = '__all__'

class HorizontalAdsForm(forms.ModelForm):
    class Meta:
        model = HorizontalAds
        fields = '__all__'

class VerticalAdsForm(forms.ModelForm):
    class Meta:
        model = VerticalAds
        fields = '__all__'

class OurTeamForm(forms.ModelForm):
    class Meta:
        model = OurTeam
        fields = '__all__'

class PrivacyPolicyForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        
class AboutUSForm(forms.ModelForm):
    class Meta:
        model = AboutUS
        fields = '__all__'
