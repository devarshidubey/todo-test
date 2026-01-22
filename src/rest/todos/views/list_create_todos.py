from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todos.services.todo_service import TodoService
from todos.serializers.todo import TodoSerializer
import sys
from rest_framework.parsers import JSONParser


print('started')
class TodoListCreateView(APIView):
    parser_classes = [JSONParser]  # optional but avoids parsing GET body

    def initial(self, request, *args, **kwargs):
        print(">>> DRF initial called")
        print("Method:", request.method)
        print("Headers:", request.headers)
        # If body exists, try to print it safely
        try:
            print("Body:", request.data)
        except Exception as e:
            print("Could not parse body:", e)
        sys.stdout.flush()
        return super().initial(request, *args, **kwargs)


    def get(self, request):
        print(">>> get() method called")  # <-- confirms GET hit
        print(request.headers)

        todos = TodoService.list_todos()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        todo = TodoService.create_todo(serializer.validated_data)

        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)