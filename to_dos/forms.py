from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo

        fields=[
            "task",
            "datetime",
            "description"
        ]  
#         
# class ComForm(forms.ModelForm):
#     class Meta:
#         model=Com

#         fields=[
#             "complited",
#         ]
      
