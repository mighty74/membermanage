from django import forms
from .models import List, BList
 
 
class DiaryForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name', 'number', 'se', 'grade', 'group', 'adre', 'content')

    def get_context_data(self, *args, **kwargs):
        #self.request = kwargs.pop("request")
        super(DiaryForm, self).get_context_data(*args, **kwargs)
        self.fields['listpk'].initial = self.kwargs['pk']
        self.fields['author'].initial = self.request.user.username

class HomeForm(forms.ModelForm):
    class Meta:
        model = BList
        fields = ('title', 'content')

    def get_context_data(self, *args, **kwargs):
        super(DiaryForm, self).get_context_data(*args, **kwargs)
        self.fields['author'].initial = self.request.user.username
