"""fzap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.OrdersListView),
    path('api/marks/<int:mark_pk>/models/<int:pk>', views.api_mark_model_detail),
    path('api/marks/<int:mark_pk>/models/', views.api_mark_models),
    path('api/marks/<int:pk>', views.api_mark_detail),
    path('api/marks/', views.api_marks),
    path('api/orders/<int:pk>', views.api_order_detail),
    path('api/orders/', views.api_orders),
    path('api/shops/<int:pk>', views.api_shop_detail),
    path('api/shops/', views.api_shops),
    path('api/answers/<int:pk>', views.api_answer_detail),
    path('api/answers/', views.api_answers),
    path('order/', views.OrderFormView),
]
