from django.urls import path
from . import views


app_name='yogastudio'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('schedule/', views.schedule, name='schedule'),
    path('course/<int:pk>', views.course_detail, name='course_detail'),
    path('book/<int:pk>', views.BookView, name='book_course'),
]