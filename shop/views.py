from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from shop.models import Product,ProductImage, Type,Feature,About,Contact_us,Category
from shop.forms import ContactCreateForm

"""
function based views 
class based views 
    View
    generic
"""


class HomePageView(View):
    def get(self, request):
        return render(request, "shop/index.html")


class AboutView(View):
    def get(self, request):
        abouts = About.objects.all().order_by("created_at")
        context = {
            "abouts": abouts,
        }
        return render(request, "shop/about.html", context=context)

class Contact_usCreateView(CreateView):
    model = Contact_us
    fields = ["name","number","reason","subject"]
    template_name = "shop/contact.html"


# class Contact_usView(View):
#     def get(self, request):
#         contacts = Contact_us.objects.all().order_by("-created_at")
#         # form = ContactCreateForm()
#         context = {
#             "contacts": contacts,
#             # "form": form
#         }
#         return render(request, "shop/contact.html", context=context)
#
#     def post(self, request):
#         contacts = Contact_us.objects.all().order_by("-created_at")
#         form = ContactCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("shop:contact-page")
#         else:
#             return render(request, "shop/contact.html", context={
#                 "contacts": contacts,
#                 "form": form
#             })


class CategoryView(View):
    def get(self,request):
        return render(request, "shop/index.html")



# class StoreListView(ListView):
#     model = Store
#     context_object_name = "stores"
#     template_name = "bookshop/store_list.html"
#
# class StoreDetialView(DetailView):
#     model= Store
#     template_name = "bookshop/store_detail.html"
#     context_object_name = "store"
#
# class StoreCreateView(CreateView):
#     model = Store
#     form = StoreCreateForm
#     fields = ["name", "books"]
#     template_name = "bookshop/store_create.html"
#
# class AuthorListView(ListView):
#     model = Author
#     context_object_name = "authors"
#     template_name = "bookshop/author_list.html"
#
# class AuthorDetialView(DetailView):
#     model= Author
#     template_name = "bookshop/author_detail.html"
#     context_object_name = "author"
#
# class AuthorCreateView(CreateView):
#     model = Author
#     form=AuthorCreateForm
#     fields = ["username", "first_name", "last_name", "age"]
#     template_name = "bookshop/author_create.html"
#
# class BookListView(ListView):
#     model = Book
#     context_object_name = "books"
#     template_name = "bookshop/book_list.html"
#
# class BookDetialView(DetailView):
#     model= Book
#     template_name = "bookshop/book_detail.html"
#     context_object_name = "book"
#
# class BookCreateView(CreateView):
#     model = Book
#     form = BookCreateForm
#     fields = ["name", "rating", "price"]
#     template_name = "bookshop/book_create.html"
#
# class BookUpdateView(UpdateView):
#     model = Book
#     form = BookUpdateForm
#     fields = ["name", "rating", "price"]
#     template_name = "bookshop/book_update.html"
