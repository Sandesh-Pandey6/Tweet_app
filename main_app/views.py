from django.http import HttpResponse


def first_page(response):
    return HttpResponse("This is the first page")