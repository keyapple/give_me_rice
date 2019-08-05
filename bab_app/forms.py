from django import forms
from .models import Post, Ingredient, Postingre, Comment
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'view_count', 'content', 'like', 'user']
        labels = {
            'title': "제목",
            'image': "이미지",
            'view_count': "조회수",
            'content': "내용",
            'like': "좋아요",
        }
        widgets = {
            'user': forms.HiddenInput(),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient', 'post', 'user']
        labels = {
            'ingredient': 재료
        }
        widgets = {
            'post': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }

class PostingreForm(forms.ModelForm):
    class Meta:
        model = Postingre
        fields = ['quantity', 'post', 'user']
        labels = {
            'quantity': 재료량
        }
        widgets = {
            'post': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }

