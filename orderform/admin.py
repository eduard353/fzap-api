from django.contrib import admin
from .models import Mark, Model, Shop, Order, Answer
# Register your models here.

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('mark_name',)
    list_filter = ('mark_name',)
    search_fields = ('mark_name',)
    ordering = ('mark_name',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model_name',)
    list_filter = ('mark', 'model_name',)
    search_fields = ('mark', 'model_name',)
    ordering = ('mark', 'model_name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'year', 'vin', 'order_details', 'date')
    list_filter = ('user', 'model', 'year', 'vin')
    search_fields = ('user', 'model', 'year', 'vin')
    ordering = ('date',)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'address', 'phone', 'email', 'description')
    list_filter = ('shop_name', 'address', 'phone', 'email')
    search_fields = ('shop_name', 'address', 'phone', 'email')
    ordering = ('shop_name',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('order', 'shop', 'answer_details', 'price', 'date')
    list_filter = ('order', 'shop', 'answer_details', 'price', 'date')
    search_fields = ('order', 'shop', 'answer_details', 'price', 'date')
    ordering = ('date',)
