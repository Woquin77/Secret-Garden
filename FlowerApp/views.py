from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Flower


@login_required(login_url='login')
def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers.html', {'flowers': flowers})


@login_required(login_url='login')
def add_flower(request):
    if request.method == "POST":
        Flower.objects.create(
            name=request.POST.get('name'),
            color=request.POST.get('color'),
            price=request.POST.get('price'),
            category=request.POST.get('category'),
        )

        return redirect('flowers')

    return render(request, 'add_flower.html', {
        'categories': Flower.CATEGORY_CHOICES
    })


@login_required(login_url='login')
def edit_flower(request, id):
    flower = get_object_or_404(Flower, id=id)
    if request.method == "POST":
        flower.name = request.POST.get('name')
        flower.color = request.POST.get('color')
        flower.price = request.POST.get('price')
        flower.category = request.POST.get('category')
        flower.save()
        return redirect('flowers')

    return render(request, 'edit_flower.html', {
        'flower': flower,
        'categories': Flower.CATEGORY_CHOICES,
    })


@login_required(login_url='login')
def delete_flower(request, id):
    flower = get_object_or_404(Flower, id=id)
    if request.method == "POST":
        flower.delete()
    return redirect('flowers')