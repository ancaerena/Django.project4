from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create-post', views.PostCreate.as_view(), name= 'post_form'),
    path('<pk>/update', views.PostUpdateView.as_view(), name= 'post_update'),
    path('<pk>/delete/', views.PostDeleteView.as_view(), name= 'post_delete'),
]
