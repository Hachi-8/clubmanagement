from club_management.models import Conditions
from django.urls import path
from . import views
app_name = 'club_management'

urlpatterns = [
    path("top_page/", views.top_page, name = "top_page"),
    path("my_page/", views.my_page, name="my_page"),
    path("practice_page/", views.practice_page, name="practice_page"),
    path("practiceform_page/", views.practiceform_page, name="practiceform_page"),
    path("matchresult_page/", views.matchresult_page, name="matchresult_page"),
    path("matchresultdetail_page/", views.matchresultdetail_page, name="matchresultdetail_page"),
    path("matchresultform_page/", views.matchresultform_page, name="matchresultform_page"),
    path("group_page/", views.group_page, name="group_page"),
]