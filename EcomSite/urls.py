



from django.urls import path
from django.contrib import admin
from EcomApp.views import AboutUs, AddToCurt, CategoryView, ContactUs, CustomLogoutView, ProductDetails, RegisterView, home, profile_view
from EcomSite import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("home/", home, name="home"),
    path("about/", AboutUs, name="about"),
    path("contact/", ContactUs, name="contact"),
    path("curt/", AddToCurt, name="curt"),
    path('admin/', admin.site.urls),
    path("category/<str:valu>/", CategoryView.as_view(), name="category"),
    path("productdetails/<int:pk>/", ProductDetails.as_view(), name="productdetails"),
    path('profile/', profile_view, name='profile'),

    #athentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path("password-change/", auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name="password-change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name="password_change_done"),

    path('logout/', CustomLogoutView.as_view(), name='logout'),


    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
