from django.shortcuts import render, HttpResponse, redirect
from FitnessStore.models import Person, custinfo, Catagory, subCatagory, products, CartDetails
from FitnessStore.forms import PersonForm, custregister

def Home(request):
    cequi = Catagory.objects.get(id=1)
    cequi1 = Catagory.objects.get(id=2)
    cequi2 = Catagory.objects.get(id=3)    
    equips = subCatagory.objects.filter(catagory=cequi)
    equips1 = subCatagory.objects.filter(catagory=cequi1)
    equips2 = subCatagory.objects.filter(catagory=cequi2)
    return render(request, "index.html", {"subcat":equips, "subcat1":equips1, "subcat2":equips2})

def ShowPersons(request):
    persons = Person.objects.all()
    return render(request, "Persons.html", {"persons": persons})

def delPerson(request,id):
    p = Person.objects.filter(id=id)
    p.delete()
    return redirect(ShowPersons)

def AddPerson(request):
    formP = PersonForm(request.POST)
    if(request.method=="GET"):
        return render(request,"addPerson.html", {})

    if(formP.is_valid):
        formP.save()
        pname = request.POST["pname"]
        plocation = request.POST["ploc"]
        formP = Person(pname,plocation)
    return redirect(ShowPersons)

def editPerson(request, id):
    p = Person.objects.get(id=id)
    if (request.method == "GET"):
        return render(request, "editperson.html", {"p":p})
    else:
        p.pname = request.POST["pname"]
        p.plocation = request.POST["ploc"]
        p.save()
        return redirect(ShowPersons)

def logout(request):
    del request.session["username"]
    return redirect(Home)

def login(request):
    if(request.method=="GET"):
        return render(request,"userlogin.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        users = custinfo.objects.filter(cmail=uname,cpass=pwd)
        if(users.count() != 0):
            #return HttpResponse("Success")
            request.session["username"]=uname
            return redirect(Home)
        else:
            return redirect(login)
    

def loginvalidate(request):
    if(request.method=="POST"):
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")        
        result = custinfo.objects.filter(cmail=uname,cpass=pwd)
        if(result != None):
            request.session["cmail"]=uname
            return redirect(Home)
        else:
            return redirect(login)


def custRegister(request):
    form = custregister(request.POST)
    if(request.method=="GET"):
        return render(request,"custregister.html",{})

    if(form.is_valid):
        form.save()
        cfname = request.POST["cfname"]
        cmail = request.POST["cmail"]
        cpass = request.POST["cpass"]
        ccontact = request.POST["ccontact"]
        form = custinfo(cfname,cmail,cpass,ccontact)
    return redirect(showCust)

def showCust(request):
    custs = custinfo.objects.all()
    return render(request, "custList.html", {"custs":custs})

###############################Products#########################################
def ShowProducts(request,id):
    cequi = Catagory.objects.get(id=1)
    cequi1 = Catagory.objects.get(id=2)
    cequi2 = Catagory.objects.get(id=3)
    equips = subCatagory.objects.filter(catagory=cequi)
    equips1 = subCatagory.objects.filter(catagory=cequi1)
    equips2 = subCatagory.objects.filter(catagory=cequi2)
    subcs = subCatagory.objects.get(id=id)
    prds = products.objects.filter(subcat=subcs)        
    return render(request, "products.html", {"subcat":equips,"prds":prds, "subcat1":equips1, "subcat2":equips2})

##########################Cart#############################################
def addToCart(request):
    if("username" in request.session):
        user = request.session["username"]
        pid = request.POST["pid"]        
        u1 = custinfo.objects.get(cmail=user)
        p1 = products.objects.get(id=pid)
        data = CartDetails.objects.filter(product=p1,user=u1)
        #product with same user is not present
        #Add item to cart
        if(data.count()==0):
            c1 = CartDetails()
            c1.user = u1
            c1.product = p1
            c1.save()
    else:
        return redirect(login)

    return redirect(ShowallCartItems)

def ShowallCartItems(request):
    user = request.session["username"]
    u1 = custinfo.objects.get(cmail=user)
    cart_items = CartDetails.objects.filter(user=u1)
    #product with same user is not present
    if(cart_items.count()!=0):
        productss = []
        total = 0
        for c in cart_items:
            p1 = products.objects.get(id=c.product.id)
            total = total + p1.prate
            productss.append(p1)
            
    
        request.session["total"] = total
        coc = len(productss)
        return render(request,"ShowallCartItems.html",{"products" : productss,"total":total, "cont":coc})
    return render(request,"ShowallCartItems.html",{})

def RemoveCartItem(request):
    user = request.session["username"]
    pid = request.POST["pid"]
    p1 = products.objects.get(id=pid)
    u1 = custinfo.objects.get(cmail=user)
    data = CartDetails.objects.get(product=p1,user=u1)
    data.delete()
    return redirect(ShowallCartItems)

