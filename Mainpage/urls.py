from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name="Homepage"),
    path('about/',views.AboutPage,name="AboutPage"),
    path('costumes/',views.Costumepage,name="Costumepage"),
    path('festival/',views.FestivalPage,name="FestivalPage"),
    path('Halloween/',views.HalloweenPage,name="HalloweenPage"),
    path('Marriage/',views.MarriagePage,name="MarriagePage"),
    path('Patriotic/',views.PatrioticPage,name="PatrioticPage"),
    path('Party/',views.PartyPage,name="PartyPage"),
    path('product/<id>',views.MyProduct,name="MyProduct"),
    path('Mycart/',views.Mycart,name="Mycart"),
    path('removeitem/',views.RemoveItem,name="RemoveItem"),
    path('profile/',views.MyProfile,name="MyProfile"),
    path('edit-profile/',views.EditProfile,name="Editprofile"),
    path('contact/',views.contactPage,name="contactPage"),
    path('logout/',views.logout_page,name="logout_page"),
    path('order/',views.OrderPage,name="OrderPage"),
    path('checkout/',views.checkout,name="checkout"),
    path('success/',views.success_page,name="success_page"),
    path('cancle/',views.cancle_page,name="cancle_page"),
    path('portfolio/',views.PortfolioPage,name="PortfolioPage"),
    path('search/',views.SearchPage,name="SearchPage"),
]