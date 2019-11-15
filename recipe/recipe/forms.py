from django import forms
from recipe.models import RecipeItem


class AddAuthor(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeItem(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = [
            'author',
            'title',
            'description',
            'time',
            'instructions'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)