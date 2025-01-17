from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Product
from .form import CreateProductForm
from .task import create_dynamic_product
import csv
from django.http import HttpResponse
from .models import Product

def get_product_listing(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "product_listing.html", {"page_obj": page_obj})


def web_create_dynamic_product(request):
    if request.method == "POST":
        form = CreateProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            create_dynamic_product(form.cleaned_data.get('number'))
            return redirect('product_listing')
    else:
        form = CreateProductForm()

    return render(request, "create_dynamic_product.html", {"form": form})



def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['title', 'description', 'price'])

    products = Product.objects.all()
    for product in products:
        writer.writerow([product.title, product.description, product.price])

    return response