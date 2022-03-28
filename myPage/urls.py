from django.urls import path
from . import views


app_name = 'myPage'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('index/<int:question_id>/', views.detail, name="detail"),
    path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),
    path('question/create/', views.question_create, name="question_create"),
]