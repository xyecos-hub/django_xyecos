from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lessons, name="lessons"),
    path('<int:pk>', views.LessonDetailView.as_view(), name="LessonDetail")
]
