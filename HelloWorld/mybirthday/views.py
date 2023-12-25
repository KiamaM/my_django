import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "mybirthday/index.html", {
        "mybirthday": now.month == 12 and now.day == 29

    })