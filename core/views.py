# Create your views here.

from django.shortcuts import render_to_response

def homepage(request):
#    return HttpResponse('Bem vindo ao EventeX!')
##    t = loader.get_template('index.html')
##    c = Context()

##    content = t.render(c)

##    return HttpResponse(content)

    from django.conf import settings
    context = {'MEDIA_URL': settings.MEDIA_URL}

    return render_to_response('index.html', context)


