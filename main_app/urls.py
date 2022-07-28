from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name="profile_update"),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('like/', views.like_post, name='like_post'),
    path('posts/<int:pk>/', views.comments_view, name='comments'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/<int:user_id>/add_comment/', views.add_comment, name="add_comment"),
    path('accounts/signup/', views.signup, name='signup'),
]
