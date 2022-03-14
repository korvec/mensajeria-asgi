from django.shortcuts import render

# Create your views here.
def sala_global(request):
    return render(request, 'chat/salaglobal.html')

def index(request):
    return render(request, 'chat/index.html')

def sala(request, room_name):
    return render(request, 'chat/sala.html', {'room_name': room_name})
