from django.urls import path
from todos.views.list_create_todos import TodoListCreateView

print(">>> todos.urls module loaded")


urlpatterns = [
    path('', TodoListCreateView.as_view(), name='list_create'),
]