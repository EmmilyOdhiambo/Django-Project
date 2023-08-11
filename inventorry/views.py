# from django.shortcuts import render
# from .forms import ProductUploadForm

# # Create your views here.
# def product_upload_view(request):
#     form = ProductUploadForm()
#     return render(request,"inventory/product_upload.html",{"form":form})

# def products_list(request):
#     products = Products.objects.all()    
#     return render(request, "inventory/products_list.html"),
# def product_detail_view(request, id):
#     product = Product.objects.get(id = id)
#     return render(request, "inventory/product_detail.html",{"product":product})

# from django.shortcuts import render
# from .forms import ProductUploadForm
# from inventorry.models import Product
# from django.shortcuts import redirect
# def product_upload_view(request):
#     if request.method == "POST":
#         form = ProductUploadForm(request.POST,request.FILES)
#         if form.is_valid():
#          form.save()
#     else:
#         form = ProductUploadForm
#     return render(request , 'inventorry/product_upload.html' , {'form':form})
    
# Create your views here.
# def products_list(request):
#    products = Product.objects.all()
#    return render(request,"inventorry/productList.html",{'product':products})

# def product_details(request, id):
#    product_dets = Product.objects.get(id=id)
#    return render(request,"inventorry/productDetails.html",{'product_dets':product_dets})

# def edit_product(request,id):
#     edit_products = Product.objects.get(id=id)
#     if request.method =='POST':
#         form = ProductUploadForm(request.POST,instance=edit_products)
#         if form.is_valid():
#             form.save()
#             return redirect('product_details,id=id')
#         else:
#             form = ProductUploadForm(instance=edit_products)
#             return render(request,'inventorry/edit_product.html',{'form':form})




from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from inventorry.models import Product

# Create your views here.
def product_upload(request):
    if  request.method == 'POST':
      form = ProductUploadForm(request.POST , request.FILES)
      if form.is_valid():
       form.save()
      
    else:
       
       form = ProductUploadForm()
    return render(request, 'inventorry/product_upload.html', {"form" : form})

def product_list(request):
    products = Product.objects.all()

    return render(request, "inventorry/product_List.html", {"products": products})

def product_details (request, id):
    product = Product.objects.get( id = id)

    return render(
        request, "inventorry/product_detail.html", {"product" : product})

# def edit_product(request,id):
#     product = Product.objects.get(id=id)

#     if request.method == 'POST':
#        form = ProductUploadForm(request.POST, instance=product)
#        if form.is_valid():
#           form.save()
#           return redirect("product_details", id=id)
#     else:
#        form = ProductUploadForm(instance=product)

#     return render (request, "inventorry/product_edit.html", {"form":form})



    