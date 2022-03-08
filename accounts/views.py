from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.


def register(request):
    form = SignUpForm (request.POST or None)

    if form.is_valid():
        form.save()
        form = SignUpForm ()

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)