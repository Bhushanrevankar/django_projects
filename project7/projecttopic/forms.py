from .models import Project 
from django.forms import ModelForm

class ProjectForm (ModelForm):

    class Meta:

        model = Project

        fields = "__all__"

        exclude=[]