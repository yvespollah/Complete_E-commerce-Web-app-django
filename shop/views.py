from django.shortcuts import render

# Create your views here.

def shop(request, *args, **kwargs):
    """vue des produit """
    context = {}
    return render(request , 'shop/index.html', context)