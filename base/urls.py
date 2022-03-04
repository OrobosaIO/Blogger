
from django.urls import path
from . import views
from .views import AddPostView, HomeView, ArticleDetailView, StandardView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name ="article-detail"), 
    path('article/<int:pk>', StandardView.as_view(), name ="standard-view"),
    path('add_post/', AddPostView.as_view(), name= 'add_post'),
    path('About', views.AboutView, name = 'About' ),
    path('Contact Us', views.ContactView, name = 'Contact Us')
]
