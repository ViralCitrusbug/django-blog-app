from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from .models import Category,Post

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']
        widgets = {
            'password':forms.PasswordInput()
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user  

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()
CreatePostForm = inlineformset_factory(Category,Post,form=PostForm)