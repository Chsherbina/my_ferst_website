from django import forms

from posts.models import Tag, Post


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search',
                'class': 'form-control',
            }))
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    ordering = (
        ('title', 'по заголовку'),
        ('-title', 'по заголовку в обратном порядке'),
        ('rate', 'по рейтенгу'),
        ('-rate', 'по рейтенгу в обратном порядке'),
        ('-created_at', 'по дате создания в обратном порядке'),
        ('created_at', 'по дате создания'),
    )
    ordering = forms.ChoiceField(
        required=False,
        choices=ordering,
        widget=forms.Select(attrs={'placeholder': 'Ordering', 'class': 'form-control'})
    )


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
