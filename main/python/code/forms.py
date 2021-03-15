from django import forms

from ...models import *
class IndexForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','count','date','memo','user',]
        widgets = {
            'date': forms.SelectDateWidget
        }

class FindIndex(forms.Form):
    find = forms.CharField(label='Find',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))



 
 
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        id = forms.IntegerField(label='ID')
        fields = ('description', 'photo',)
