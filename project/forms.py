from django.db import models
from django import forms
from django.forms import ModelForm
from .models import collab_project







class CreateNewProject(forms.ModelForm):


    class Meta:
        model = collab_project
        fields=['p_name','p_desc','p_prerequisite','p_part','p_category','p_level','p_image']




# class CreateNewProject(forms.Form):
#     p_name=forms.CharField(label="Project Name", max_length=75)
#     p_desc=forms.CharField(label="Description", max_length=200)
#     # p_level=forms.ForeignKey(label="Level")
#     # p_category=forms.ForeignKey(label="Category")
#     p_parts=forms.IntegerField(label="No. of Participants")
#     p_image=forms.ImageField(label="Upload Image")
#
#     #
#     # p_name=models.CharField(max_length=75)
#     # p_desc=models.CharField(max_length=200)
#     # # p_level=models.ForeignKey(level, on_delete=models.CASCADE)
#     # # p_category=models.ForeignKey(category, on_delete=models.CASCADE)
#     # p_image=models.ImageField(upload_to="account/media",default="")
#     # p_part=models.IntegerField()
