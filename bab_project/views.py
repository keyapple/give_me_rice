from django.shortcuts import render
import pdb

def home(request):
    return render(request, 'bab_app/index.html')