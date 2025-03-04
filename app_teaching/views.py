from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import PandasClass

# ویو برای نمایش صفحه اصلی و قابلیت مشاهده پست‌ها با دکمه‌های قبل و بعد
def index_view(request):
    classes = list(PandasClass.objects.filter(status='published', published__lte=timezone.now()).order_by('-published'))

    # ایندکس پست فعلی را از URL دریافت کنیم (پیش‌فرض: ۰)
    index = int(request.GET.get('index', 0))

    # کنترل محدوده ایندکس
    if index < 0:
        index = 0
    elif index >= len(classes):
        index = len(classes) - 1

    # گرفتن پست جاری
    current_post = classes[index] if classes else None

    # تعیین مقادیر قبلی و بعدی
    previous_index = index - 1 if index > 0 else None
    next_index = index + 1 if index < len(classes) - 1 else None

    return render(request, 'index.html', {
        'current_post': current_post,
        'previous_index': previous_index,
        'next_index': next_index,
        'classes': classes,
    })

# ویو برای نمایش لیست تمام پست‌ها
def pandas_class_list(request):
    classes = PandasClass.objects.filter(status='published', published__lte=timezone.now()).order_by('-published')
    return render(request, 'class_list.html', {'classes': classes})

# ویو برای نمایش جزئیات هر پست
def pandas_class_detail(request, slug):
    pandas_class = get_object_or_404(PandasClass, slug=slug, status='published', published__lte=timezone.now())

    # افزایش بازدید
    pandas_class.views += 1
    pandas_class.save(update_fields=['views'])


    return render(request, 'class_detail.html', {
        'pandas_class': pandas_class
    })