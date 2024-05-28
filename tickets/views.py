from django.shortcuts import render

from tickets.forms import CommentForm
from tickets.table import UserModel


# Create your views here.

def get_tickets_page(request):
    if request.method == "POST":
        if not UserModel.exists():
            UserModel.create_table(wait=True)
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = UserModel(name=form.cleaned_data['name'], comment=form.cleaned_data['comment'])
            user.save()

    form = CommentForm()
    return render(request, "ticket/tickets.html", {"tickets": list(UserModel.scan()), "form": form})
