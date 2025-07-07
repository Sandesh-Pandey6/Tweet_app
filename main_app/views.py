from django.http import HttpResponse


def first_page(response):
    return HttpResponse("This is the first page and to find the project go to the sub_app folder")
    return render 