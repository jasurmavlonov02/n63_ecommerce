from django.urls import path
from .views import CustomerList,CustomerDetail,exporting_data
app_name = 'customer'


urlpatterns = [
    path('',CustomerList.as_view(),name='customer_list'),
    path('detail/<int:pk>',CustomerDetail.as_view(),name='customer_detail'),
    path('export/data/',exporting_data,name='export_data')
]
