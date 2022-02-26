from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name="dash"),
    path('vote/', views.votes, name="vote"),
    path('<int:pk>/', views.Vote,name="Vote"),
    path('result/',views.Result,name="Result"),
    path('feedback/',views.Feedback,name="feedback"),
]

