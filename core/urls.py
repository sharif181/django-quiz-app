from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.Quiz.as_view(),name="quiz"),
    path('r/<str:topic>',views.RandomQuestion.as_view(),name="random")
]