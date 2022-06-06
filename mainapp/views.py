from django.shortcuts import render
from requests import request
from .forms import CaptchaForm
from django.contrib import messages

def IndexView(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request, 'کپچا صحیح است')
        else:
            messages.error(request, 'غلط! دوباره امتحان کنید')
    form = CaptchaForm
    return render(request, 'index.html', {'form':form})