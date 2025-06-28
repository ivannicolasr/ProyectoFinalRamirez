from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', login_required(PostCreateView.as_view()), name='post_create'),
    path('<int:pk>/edit/', login_required(PostUpdateView.as_view()), name='post_edit'),
    path('<int:pk>/delete/', login_required(PostDeleteView.as_view()), name='post_delete'),
]