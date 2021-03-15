from django.urls import path
from . import views

from .views import SignUpView    
from main import views as v1
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('',v1.Top,name='Top'),

]


