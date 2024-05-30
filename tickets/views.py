from django.shortcuts import render

from tickets.forms import CommentForm
from tickets.table import UserModel
from django.views.decorators.csrf import csrf_exempt

from yandex_practicum_cse import settings


# Create your views here.


@csrf_exempt
def get_tickets_page(request):
    if not UserModel.exists():
        UserModel.create_table(read_capacity_units=100, write_capacity_units=100, wait=True)

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = UserModel(name=form.cleaned_data['name'], comment=form.cleaned_data['comment'])
            user.save()

    form = CommentForm()
    return render(request, "ticket/tickets.html", {"tickets": list(UserModel.scan()), "form": form, "version": settings.VERSION})
