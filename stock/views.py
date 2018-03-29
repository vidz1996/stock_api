from django.shortcuts import render
from .tasks import get_data
from .models import ticker
# Create your views here.

def index(request):
    sd = ticker.objects.order_by('symbol')
    context_dict = {'sd':sd}
    return render(request,'index.html',context_dict)
