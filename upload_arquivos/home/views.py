from django.shortcuts import render,HttpResponse
from PIL import Image
import os
from django.conf import settings

from .models import Instrumento_Cliente

# Create your views here.
def home(request):
    if request.method == "GET":
        return render (request, 'home/home.html')
    if request.method == "POST":
        file_my = request.FILES.get('my_file')
        # print(file_my)
        # img = Image.open(file_my)
        # path = os.path.join(settings.BASE_DIR, f'media/teste.png')
        # img = img.save(path)

        mf = Instrumento_Cliente(nome="teste",caminho_arq=file_my)
        mf.save()


        sql = "show tables;"        
        #InMemoryUploadedFile --> fica na memória RAM do computador.
        # qdo o arquivo tem até 2.5 MegaBytes, o Django vai utilizar o randle de memória RAM
        # qdo tem mais de 2.5 Mega vai para o disco rígido

        # dá para mudar a memória

        return HttpResponse("Arquivo recebido.")