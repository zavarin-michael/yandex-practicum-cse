from django.shortcuts import render

from tickets.table import UserModel


# Create your views here.

def get_tickets_page(request):
    return render(request, "ticket/tickets.html", {"tickets": list(UserModel.scan())})
