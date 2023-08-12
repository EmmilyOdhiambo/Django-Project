from django.shortcuts import render

# Create your views here.

def create_account(request):
    if request.method=="POST":
     form=ProductUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=ProductUploadForm()
    return render(request,'inventory/product_upload.html',{'form':form})
