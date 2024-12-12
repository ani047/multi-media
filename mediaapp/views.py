from django.shortcuts import render
from mediaapp.forms import MediaForm
# Create your views here.


def Index(request):
    form = MediaForm()
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            print('validate')
            form.save()
    return render(request,'index.html',{'form':form})