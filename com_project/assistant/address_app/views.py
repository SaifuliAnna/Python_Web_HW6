from django.shortcuts import render, redirect

from .models import Contact, Info


# Create your views here.
def main(request):
    contacts = Contact.objects.all()
    return render(request, 'address_app/index.html', {"contacts": contacts})


def contact(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        phone = request.POST['phone']
        if nickname and phone:
            ct = Contact(nickname=nickname, phone=phone)
            ct.save()
        return redirect(to='/address_app/info/')
    # return render(request, 'address_app/info.html', {})
    return render(request, 'address_app/contact.html', {})


def info(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        birthday = request.POST['birthday']
        address = request.POST['address']
        if nickname and name and surname and email and birthday and address:
            inf = Info(nickname=nickname, name=name,
                       surname=surname, email=email, birthday=birthday, address=address)
            inf.save()
        return redirect(to='/address_app/')
    return render(request, 'address_app/info.html', {})
