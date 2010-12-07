# Create your views here.



from django.http import HttpResponse
from django.template import loader, Context



def homepage(request):
#    return HttpResponse('Bem vindo ao EventeX!')
    t = loader.get_template('index.html')
    c = Context()

    content = t.render(c)

    return HttpResponse(content)
