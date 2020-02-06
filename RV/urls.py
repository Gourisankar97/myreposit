from django.contrib import admin
from django.urls import path,include
from . import views
import re
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('movie_details/<int:id>',views.movie_details, name='movie_details'),
    path('movie_details/review',views.review),
    path('register',views.User_registration,name='User_registration'),
    path('loginpage',views.loginpage),
    path('login',views.login),
    path('review',views.review),
    path('mregister',views.mregister),
    path('mloginpage', views.mloginpage),
    path('mlogin', views.mlogin),
    path('quiz',views.quiz),
    path('quizstart',views.quizstart),
    path('endquiz', views.endquiz)
]
