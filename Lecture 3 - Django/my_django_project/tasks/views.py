from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class TaskForm(forms.Form):
    task = forms.CharField(label='Task', max_length=100)

# Create your views here.
def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session['tasks']
    })

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            if 'tasks' not in request.session:
                request.session['tasks'] = []
            request.session['tasks'] += [task]
            request.session.modified = True
            return HttpResponseRedirect(reverse('tasks:index'))
    else:
        return render(request, 'tasks/add.html', {
            "form": TaskForm()
        })