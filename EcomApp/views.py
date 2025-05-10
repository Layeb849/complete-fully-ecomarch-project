from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import  product
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def home(request):
    products = product.objects.all() 
    return render(request, 'home.html',{'products': products})

def AboutUs(request):
    return render(request, 'about.html')

def AddToCurt(request):
    return render(request, 'cart.html')

def ContactUs(request):
    return render(request, 'contact.html')

class CategoryView(View):
    def get(self, request, valu):
        products = product.objects.filter(category=valu)
        return render(request, 'category.html', {'products': products})


class CategoryTitle(View):
    def get(self, request, valu):
        products = product.objects.filter(title=valu)
        title = product.objects.filter(category=product[0].category).values('title')
        return render(request, 'category.html', {'products': products})


class ProductDetails(View):
    def get(self, request, pk):
        single_product = product.objects.get(pk=pk)
        return render(request, 'product_details.html', {'product': single_product})

#authentication

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
        return render(request, 'register.html', {'form': form})



class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
    


@login_required
def profile_view(request):
    return render(request, 'profile.html')

























# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, "product_detail.html", {"product": product})

# # 🟢 নতুন Product Add করার ফাংশন (পুরনো ডাটা ডিলিট হবে না)
# def add_product(request):
#     if request.method == "POST":
#         name = request.POST["name"]
#         description = request.POST["description"]
#         price = request.POST["price"]
#         category_id = request.POST["category"]
#         stock = request.POST["stock"]
#         image = request.FILES.get("image")  # নতুন ইমেজ নিলে সেট করবে

#         category = get_object_or_404(Category, id=category_id)

#         # 🔵 নতুন প্রোডাক্ট তৈরি করবে
#         Product.objects.create(
#             name=name,
#             description=description,
#             price=price,
#             category=category,
#             stock=stock,
#             image=image
#         )
#         messages.success(request, "Product added successfully!")
#         return redirect("home")  # ✅ Home পেজে রিডাইরেক্ট করো

#     categories = Category.objects.all()  # ক্যাটাগরি লোড করো
#     return render(request, "add_product.html", {"categories": categories})

# # 🟢 Product Edit করার ফাংশন
# def edit_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == "POST":
#         product.name = request.POST["name"]
#         product.description = request.POST["description"]
#         product.price = request.POST["price"]
#         product.category_id = request.POST["category"]
#         product.stock = request.POST["stock"]

#         # ✅ যদি নতুন ইমেজ দেওয়া হয়, তাহলে পুরাতো ইমেজ ডিলিট না করেই আপডেট করো
#         if "image" in request.FILES:
#             product.image = request.FILES["image"]

#         product.save()
#         messages.success(request, "Product updated successfully!")
#         return redirect("home")

#     categories = Category.objects.all()
#     return render(request, "edit_product.html", {"product": product, "categories": categories})

# # 🟢 Product Delete করার ফাংশন
# def delete_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     product.delete()
#     messages.success(request, "Product deleted successfully!")
#     return redirect("home")

# # 🟢 কার্টে প্রোডাক্ট যোগ করার ফাংশন
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     session_id = request.session.session_key

#     if not session_id:
#         request.session.create()
#         session_id = request.session.session_key

#     cart_item, created = Cart.objects.get_or_create(
#         session_id=session_id,
#         product=product
#     )
#     cart_item.quantity += 1  # যদি একই প্রোডাক্ট থাকে তাহলে সংখ্যা বাড়াবে
#     cart_item.save()

#     messages.success(request, "Product added to cart!")
#     return redirect("home")

# # 🟢 কার্ট দেখানোর ফাংশন
# def view_cart(request):
#     session_id = request.session.session_key
#     cart_items = Cart.objects.filter(session_id=session_id)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)

#     return render(request, "cart.html", {"cart_items": cart_items, "total_price": total_price})

# # 🟢 কার্ট থেকে প্রোডাক্ট মুছে ফেলার ফাংশন
# def remove_from_cart(request, cart_id):
#     cart_item = get_object_or_404(Cart, id=cart_id)
#     cart_item.delete()
#     messages.success(request, "Product removed from cart!")
#     return redirect("view_cart")

# # 🟢 অর্ডার প্লেস করার ফাংশন
# def place_order(request):
#     session_id = request.session.session_key
#     cart_items = Cart.objects.filter(session_id=session_id)

#     if not cart_items:
#         messages.warning(request, "Your cart is empty!")
#         return redirect("home")

#     total_price = sum(item.product.price * item.quantity for item in cart_items)

#     if request.method == "POST":
#         name = request.POST["name"]
#         email = request.POST["email"]
#         address = request.POST["address"]

#         order = Order.objects.create(
#             name=name,
#             email=email,
#             address=address,
#             total_price=total_price
#         )

#         cart_items.delete()  # ✅ কার্ট খালি করে দেবে
#         messages.success(request, "Order placed successfully!")
#         return redirect("home")

#     return render(request, "place_order.html", {"cart_items": cart_items, "total_price": total_price})
