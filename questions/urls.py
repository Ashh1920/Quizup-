from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('view_score',views.view_score,name='view_score'),
    path('api/check_score',views.check_score,name='check_score'),
    path('<id>',views.take_quiz,name='take_quiz'),
    path('api/<id>' , views.api_question ,name='api_question'),
   
]