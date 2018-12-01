"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from django.urls import path
# from django.shortcuts import HttpResponse,render
from app01 import views

# def login1(request):
#     """
#     :param request:  所有请求相关的数据都封装在request对象里面
#     :return:
#     """
#     # return HttpResponse("ok")
#     return render(request,'login1.html')
#
# def index1(request):
#     return render(request,'index1.html')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login1/$',views.login1),
    url(r'^index1/$',views.index1),
    url(r'^press_list/$',views.press_list),  # 展示出版社
    url(r'^add_press/$',views.add_press),  # 添加出版社
    url(r'^delete_press/$',views.delete_press),  # 删除出版社
    url(r'^edit_press/$',views.edit_press),  # 编辑出版社

    url(r'^book_list/$',views.books),  # 展示书籍列表
    url(r'^add_book/$',views.add_book),  # 添加书籍
    url(r'^delete_book/$',views.delete_book),  # 删除书籍
    url(r'^edit_book/$',views.edit_book),  # 编辑书籍

    url(r'^author_list/$',views.author_list),  # 作者列表
    url(r'^add_author/$',views.add_author),  # 添加作者
    url(r'^delete_author/$',views.delete_author),  # 删除作者
    url(r'^edit_author/$',views.edit_author),  # 编辑作者

    url(r'^upload/$',views.upload)  #上传文件
]
