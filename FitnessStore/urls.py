from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from FitnessStore import views

urlpatterns = [
    path('index/', views.Home),
    path('persons/delP/<int:id>', views.delPerson),
    path('custRegister/', views.custRegister),
    path('persons/', views.ShowPersons),
    path('addPerson/', views.AddPerson),
    path('custlist/', views.showCust),
    path('persons/editp/<int:id>', views.editPerson),
    path('userlogin/', views.login),
    path('logout/',views.logout),
    path('ShowProducts/<id>', views.ShowProducts),
    path('addtocart/', views.addToCart),
    path('showcart/', views.ShowallCartItems),
    path('removefromcart/', views.RemoveCartItem)
]