from django.shortcuts import render
def view_name(request):
    return render(request, 'test.html', {})
# Create your views here.
