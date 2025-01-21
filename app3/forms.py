from django import forms
from .models import Project

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'url']
# from django import forms
# from .models import Projec

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Projec
#         fields = ['title', 'description']  # Add other fields as needed
        
from django import forms
from .models import Mynews

class MynewsForm(forms.ModelForm):
    class Meta:
        model = Mynews
        fields = ['title', 'image', 'pdf']  # Specify the fields to be included in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})  # Add CSS class for styling
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})  # Add CSS class for styling
        self.fields['pdf'].widget.attrs.update({'class': 'form-control-file'})  # Add CSS class for styling
