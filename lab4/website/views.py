from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from .models import Person


# Create your views here.

def home(request):
    return render(request, 'website.html', {})


def person_view(request):
    if request.method == 'GET':
        try:
            person_id = request.GET.get('person_id')
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            raise Http404

        return HttpResponse(f"GET {person.fio}", status=200)

    if request.method == 'POST':
        try:
            person_id = request.POST.get('person_id')
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            raise Http404

        return HttpResponse(f"POST {person.fio}")
