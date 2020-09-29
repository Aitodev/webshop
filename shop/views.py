from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# from cart.forms import CartAddProductForm
from django.views import View
from blog.models import Blog
from django.core.mail import send_mail
import telebot
from .forms import ApplicationsForm
from django.views.generic import ListView


bot = telebot.TeleBot("1314657102:AAGbNCKRR3u0IS10sU42DO1XGFKCKNxmVDY")


def index(request):
    return render(request, 'shop/index.html')


def shop(request):
    return render(request, 'shop/shop.html')

def my_account(request):
	return render(request, 'shop/account.html')

def shopping(request):
	return render(request, 'cart/shopping-cart.html')

def checkout(request):
	return render(request, 'shop/checkout.html')

def contact(request):
    form = ApplicationsForm()
    return render(request, 'shop/contact.html', {'form': form})

def blog(request):
	return render(request, 'shop/blog.html')

def wishlist(request):
	return render(request, 'shop/wishlist.html')

def detail(request):

	# productdetail = get_object_or_404(productdetail, pk=pk)
	# context = {
	# 'productdetail': prod
	# }
	return render(request, 'shop/product-details.html')			

def shop(request):
	product = Product.objects.all()
	return render(request, 'shop/shop.html', {'producent': product})	

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog.html', context)

# def category(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'shop/product/shop.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})


# def product_details(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product-details.html', {'product': product,
#                                                         'cart_product_form': cart_product_form})
class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            # print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Новая заявка!'
            from_email = 'kiroskost@gmail.com'
            to_email = ['aitofullstackdev@gmail.com', 'aitolivelive@gmail.com']
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + comment
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(879505800, message)
        return redirect('shop:contact')
