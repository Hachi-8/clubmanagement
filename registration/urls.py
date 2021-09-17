from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'registration'

urlpatterns = [
    path("create_account/", views.create_account, name="createAccount_page"),
    path("login_done/", views.login_done, name="loginDone_page"),    
]