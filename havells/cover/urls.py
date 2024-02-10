from django.urls import path
from . import views
from .views import CategoryView

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category')
]
