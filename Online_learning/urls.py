"""Online_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

import xadmin

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),

    # # 用户操作管理，URL
    # url(r'^opera/', include('apps.operation.urls', namespace='opera')),
    # # 课程机构相关 URL
    # url(r'^org/', include('apps.organizations.urls', namespace='org')),
    # # 课程相关 URL 配置
    # url(r'^course/', include('apps.courses.urls', namespace='courses')),
    # # 用户中心 URL 配置
    url(r'^users/', include('apps.users.urls'), name='users'),

]
