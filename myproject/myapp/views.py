from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

# Create
def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'myapp/create_item.html')

# Read
def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'myapp/item_detail.html', {'item': item})

# Update
def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('item_list')
    return render(request, 'myapp/update_item.html', {'item': item})

# Delete
def delete_item(request, id):
    try:
        item = Item.objects.get(id=id)
        item.delete()
        return redirect('item_list')
    except Item.DoesNotExist:
        return HttpResponseNotFound("Item not found, cannot delete.")