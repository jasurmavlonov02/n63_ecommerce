from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.core.paginator import Paginator


from .models import Category,Product,Attribute
# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'ecommerce/index.html',context)


class Index(View):
    def get(self,request,category_slug=None):
        categories = Category.objects.all()
        products = Product.objects.all()
        paginator = Paginator(products,3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'categories':categories,
            'page_obj':page_obj
        }
        if category_slug:
            products = Product.objects.filter(category__slug = category_slug)
            context = {
                'products':products,
            }
            return render(request,'ecommerce/product-list.html',context)
        
        return render(request,'ecommerce/index.html',context)
      
        
    
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'ecommerce/product-detail.html'   
    pk_url_kwarg = 'product_id'

