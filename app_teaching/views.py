from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import PandasClass

# ویو برای نمایش صفحه اصلی
def index_view(request):
    return render(request, 'index.html')

# ویو برای نمایش لیست تمام پست‌ها
def pandas_class_list(request):
    classes = PandasClass.objects.filter(status='published', published__lte=timezone.now()).order_by('-published')
    return render(request, 'class_list.html', {'classes': classes})

# ویو برای نمایش جزئیات هر پست
def pandas_class_detail(request, slug):
    pandas_class = get_object_or_404(PandasClass, slug=slug, status='published', published__lte=timezone.now())
    
    # افزایش بازدید فقط زمانی که کاربر وارد صفحه جزئیات می‌شود
    pandas_class.views += 1
    pandas_class.save(update_fields=['views'])  # فقط فیلد views آپدیت می‌شود

    return render(request, 'class_detail.html', {'pandas_class': pandas_class})
