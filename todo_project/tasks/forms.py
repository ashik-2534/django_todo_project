from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'from-control', 'rows': 3
    }))
    completed = forms.BooleanField(required=False)