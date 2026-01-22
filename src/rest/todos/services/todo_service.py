from todos.models.todo import Todo
from todos.tasks.metadata_task import add_metadata

class TodoService:

    @staticmethod
    def create_todo(data):
        todo = Todo.objects.create(**data)
        add_metadata.delay(todo.id)
        return todo
    
    @staticmethod
    def list_todos():
        return Todo.objects.all()
    
    @staticmethod
    def get_todo(id):
        return Todo.objects.filter(id=id).first()