from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from main_app.models import *


# Create your views here.


def calculator(request):
    try:
        result = {}
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                result = n1 + n2;
            elif opr == "*":
                result = n1 * n2;
            elif opr == "-":
                result = n1 - n2;
            elif opr == "/":
                result = n1 / n2;
        print(result)

    except Exception as e:
        result = "Invalid Operations........."

    dict = {'result': result,'n1':n1,'n2':n2}

    return render(request, 'index.html', context=dict)
