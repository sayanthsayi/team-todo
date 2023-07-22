from django import forms
from django.forms import ModelForm
from .models import TodoModel

class TodoForm(ModelForm):
    task = forms.CharField(max_length=250,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter task here ..."}))
    class Meta:
        model=TodoModel
        fields='__all__'
        exclude=['user','completed']
