from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from .views import (
    HomeView,
    CreatePostView,
    PostDetailView,
    PostUpdateView,
    CategoryView,
    AllPostsView,
    SearchView,
    generate_gpt_input_value,
    answer_question_with_GPT,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),

    path("all-posts/", AllPostsView.as_view(), name="all-posts"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new", CreatePostView.as_view(), name="post-create"),
    path("post/<slug:slug>/update", PostUpdateView.as_view(), name="post-update"),
    path("category/<slug:slug>/", CategoryView.as_view(), name="blog-category"),
    path("search/", SearchView.as_view(), name="blog-search"),
    path("answer-with-gpt/", answer_question_with_GPT, name="answer-with-gpt"),
    path("generate-with-gpt/", generate_gpt_input_value, name="generate-with-gpt"),

]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)