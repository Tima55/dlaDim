from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person

# Получение данных из базы данных
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

# Сохранение данных в базе данных
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.surname = request.POST.get("surname")
        person.email = request.POST.get("email")
        person.age = request.POST.get("age")
         # Проверка возраста
        try:
            age = int(person.age)
            if age < 18 or age > 65:
                return HttpResponse("Возраст должен быть от 18 до 65 лет.", status=200)  # Возвращаем успешный статус, но не сохраняем данные
        except ValueError:
            return HttpResponse("Некорректное значение возраста.", status=400)

        person.save()
    return HttpResponseRedirect("/")

# Изменение данных в базе данных
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.surname = request.POST.get("surname")
            person.age = request.POST.get("age")

            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

# Удаление данных из базы данных
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

# Обновление данных в базе данных
def update(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.surname = request.POST.get("surname")
            person.age = request.POST.get("age")

            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")