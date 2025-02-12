from django.urls import path
from app_teaching.views import *
urlpatterns = [
    path('', index_view, name='index_view'),  # نمایش صفحه اصلی
    path('classes/', pandas_class_list, name='pandas_class_list'),  # نمایش لیست تمام پست‌ها
    path('<slug:slug>/', pandas_class_detail, name='pandas_class_detail'),  # نمایش جزئیات هر پست با استفاده از slug
]
