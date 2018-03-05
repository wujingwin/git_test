from django import HttpResponse

def index(resquest):
    return HttpResponse('index page')
