from django import forms
from .models import Todo
from .models import Com

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo

        fields=[
            "task",
            "datetime",
            "description"
            
        ]
class ComForm(forms.ModelForm):
    class Meta:
        model=Com

        fields=[
            "complited"
        ]
      
