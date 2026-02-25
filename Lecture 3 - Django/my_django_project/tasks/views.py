from django.shortcuts import render

tasks = ["Buy groceries", "Clean the house", "Pay bills", "Go to the gym"]
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })

def add(request):
    return render(request, 'tasks/add.html')