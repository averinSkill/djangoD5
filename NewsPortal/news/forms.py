from django.forms import ModelForm, Textarea
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'type_post')
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

