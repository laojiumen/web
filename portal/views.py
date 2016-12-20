# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .models import BigGod,Tag


# Create your views here.

def index(request):
    content = {
        'title': u'九门',
        'biggods': get_list_or_404(BigGod)
    }
    return render(request, 'portal/index.html', content)


@require_http_methods(["POST"])
def add_tag(request, god_id):
    new_tag = request.POST['new_tag'].encode('utf-8')

    new_tag = Tag(label=new_tag)
    new_tag.save()

    biggod = BigGod.objects.get(pk=int(god_id))
    biggod.tags.add(new_tag)
    biggod.save()
    return redirect(reverse('index'))
