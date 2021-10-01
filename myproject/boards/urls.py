from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("<int:pk>/", views.board_topics, name="board_topics"),
    path("<int:pk>/new_topic", views.add_new_topic, name="add_new_topic"),
]