from celery import shared_task
from todos.models.todo import Todo
import time

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 3})
def add_metadata(self, id):
    time.sleep(10)
    todo = Todo.objects.filter(id=id).first()
    if not todo:
        return
    
    todo.metadata = {
        "key": "metadata worker task"
    }
    todo.save()