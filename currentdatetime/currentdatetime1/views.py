from django.http import HttpResponse
import datetime as dt 

def current_datetime(request):
    now=dt.datetime.now()
    html="<html><body>It is  now %s!!</body></html>"%now
    return HttpResponse(html)
