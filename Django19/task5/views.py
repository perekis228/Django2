from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Comix, Test
from .forms import Pages

# Create your views here.
pages = 3
def main(request):
    global pages
    if request.method == 'POST':
        form = Pages(request.POST)
        if form.is_valid():
            pages = int(form.cleaned_data['pages'])
    comixes = Comix.objects.all().order_by('-year')
    paginator = Paginator(comixes, pages)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main.html', {'page_obj': page_obj})

def test(request):
    return render(request, 'menu.html')