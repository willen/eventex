# Create your views here.

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscription.forms import SubscriptionForm
from subscription.models import Subscription
from subscription.utils import send_subscription_email

#def subscribe(request):
#    form = SubscriptionForm()
#    context = RequestContext(request, {'form': form})
#    return render_to_response('subscription/new.html', context)

#def subscribe(request):
#    if request.method == 'POST':
#        form = SubscriptionForm(request.POST)
#        if form.is_valid():
#            subscription = form.save()
#            return HttpResponseRedirect(
#            reverse('subscription:success', args=[subscription.pk])
#        )
#    else:
#        form = SubscriptionForm()
#    
#    context = RequestContext(request, {'form': form})
#    return render_to_response('subscription/new.html', context)

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)
    
    subscription = form.save()
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))

def success(request, id):
    subscription = get_object_or_404(Subscription, pk=id)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)


