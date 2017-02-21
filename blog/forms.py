from django import forms
from .models import Post
from .models import Page

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'visited', 
                  'memory', 'detail_image', 'extra_img_one',
                  'extra_img_two', 'post_text')

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('visited', 'memory', 'main_text', 
                  'top_image_left', 'top_image_right')