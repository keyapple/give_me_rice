from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import pdb

def browserecipes(request):
    return render(request, 'bab_app/browse-recipes.html')
  

def contact(request):
    return render(request, 'bab_app/contact.html')


def productpage(request):
    return render(request, 'bab_app/product-page.html')


def recipepage(request):
    return render(request, 'bab_app/recipe-page-1.html')


def shortcodes(request):
    return render(request, 'bab_app/shortcodes.html')


def submitrecipe(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        ingredient = request.POST.get('ingredient')
        quantity = request.POST.get('quantity')
        post = Post.objects.create(title=title, content=content, image=image)
        a = Ingredient.objects.create(ingredient_name=ingredient_name)
        b = Postingre.objects.create(quantity=quantity)
        for x,y in (a, b):
            ingredient=x, postingre=y
        pdb.set_trace()
        return redirect('home')
    return render(request, 'bab_app/submit-recipe.html')


def typography(request):
    return render(request, 'bab_app/typography.html')


