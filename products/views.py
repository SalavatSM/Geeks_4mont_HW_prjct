from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView

from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from products.constants import PAGINATION_LIMIT

# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


class MainPageCBV(ListView):
    model = Product
    template_name = 'layouts/index.html'


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        if search:
            products = products.filter(title__icontains=search)

        if search:
            products = products.filter(description__icontains=search)

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page+1)
        }
        return render(request, 'products/products.html', context=context)


class ProductCBV(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products/products.html'

    def get(self, request, *args, **kwargs):
        products = self.queryset
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        if search:
            products = products.filter(title__icontains=search)

        if search:
            products = products.filter(description__icontains=search)

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)


class ProductDetailCBV(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get(self, request, *args, **kwargs):
        product = self.queryset

        context = {
            'product': product,
            'reviews': product.review_set.all()
        }

        return render(request, self.template_name, context=context)




def product_create_view(request):
    if request.method == 'GET':

        context = {
            'form': ProductCreateForm
        }

        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


def review_create_view(request):
    if request.method == 'GET':

        context = {
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ReviewCreateForm(data, files)

        if form.is_valid():
            Review.objects.create(
                # image=form.cleaned_data.get('image'),
                text=form.cleaned_data.get('text')
            )
            return redirect('/review/')

        return render(request, 'products/detail.html', context={
            'form': form
        })



