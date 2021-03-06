from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        Note.objects.create(title=title, content=content).save()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def delete(request):
    if request.method == "POST":
        id_ = request.POST.get("delete")
        Note.objects.get(id=id_).delete()
        return redirect('index')


def update(request):
    if request.method == "POST":
        id_ = request.POST.get("update")
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note.objects.get(id=id_)
        note.title = title
        note.content = content
        note.save()
        '''
        id_ = request.POST.get("update")
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        Note.objects.update(id=id_, title=title, content=content).save()'''
        return redirect('index')