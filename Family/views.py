
from multiprocessing import context
from re import U
from django.shortcuts import render
from Family.models import Family

def persona(request):
    persona_1= Family.objects.create(name= "lucas", last_name= "badino", age = 25, Dni=39472312, date_of_birth =17/9/1996)
    persona_2= Family.objects.create(name= "juan pablo", last_name= "badino", age = 28, Dni=20085155, date_of_birth =17/9/1999)
    persona_3= Family.objects.create(name= "santiago", last_name= "badino", age = 18, Dni=36985214, date_of_birth =17/9/1992)

    context = {
        "new_person": persona_1,
        "new_person_2":persona_2,
        "new_person_3":persona_3
    }
    return render(request, "family.html", context=context)

def todos(request):
    all_people = Family.objects.all()
    context= {
        "personas": all_people
    }
    return render(request, "all.html", context=context)

