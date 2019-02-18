from django.urls import path

from apis import views

app_name='apis'
urlpatterns=[
    path('questions',views.QuestionList.as_view())    
]