from django import HttpResponse

def index(resquest):
    return HttpResponse('index page')

def home(reuqest):
    return HttpResponse('home page')
