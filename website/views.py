from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == "POST":
        # do stuff
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']

        # send mail
        send_mail(
        email, # from mail
        comments, # message
        name, # subject
        ['mansoor.salari2021@gmail.com'], #to mail
        fail_silently=False,
        )

        return render(request, 'contact.html', {'name':name})
    # return the page
    else:
        return render(request, 'contact.html', {})
