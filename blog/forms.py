from django import forms
from .models import Post, Category
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "meta_description", "meta_image", "meta_alt_text", "content", "snippet"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "meta_description": forms.Textarea(attrs={"class": "form-control"}),
            "meta_image": forms.FileInput(attrs={"class": "form-control"}),
            "meta_alt_text": forms.TextInput(attrs={"class": "form-control"}),
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"

            ),
            "snippet": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["category"].choices = [(category.id, category.name) for category in Category.objects.all()]
        # self.fields["snippet"].validators.append(snippet_validator)