from django.http import HttpResponse

def home(request):
    return HttpResponse("Добре дошли в моето Django приложение!")
