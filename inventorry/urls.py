# from django.urls import path
# from .views import product_upload_view, products_list, product_details

# urlpatterns = [
#     path("products/upload/",product_upload_view),
#     path("products/list", products_list, name = "products_list_view"),
#     path ("products/<int:id>/", product_details, name="product_detail")
# ]
from django.urls import path
from inventorry.views import product_upload, product_list, product_details
# from .views import product_upload,product_list,product_details
from .import views




urlpatterns = [
    # path('products/upload', upload_product, name='product_upload_view'),
    path("products/upload/",product_upload),
    path("products/list",product_list,name= "product_list_view"),
    path("products/<int:id>/", product_details, name="product_detail_view"),
    # path("products/edit/<int:id>", edit_product, name="product_edit_view"),
    ]