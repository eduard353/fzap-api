from django.shortcuts import render
from .models import Order, Mark, Model, Shop, Answer
from .forms import OrderForm, MarkForm
from django.http import JsonResponse
from .serializers import MarkSerializer, ModelSerializer, OrderSerializer, ShopSerializer, AnswerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def OrdersListView(request):
    """ Представление списка заказов """
    orders_list = Order.objects.all()

    return render(request, 'orders_list.html', {'orders': orders_list})


@api_view(['GET', 'POST'])
def api_marks(request):
    """API представление всех Марок автомобилей"""
    if request.method == 'GET':
        marks = Mark.objects.all()
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def api_mark_detail(request, pk):
    """API представление одной Марки автомобилей"""
    mark = Mark.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = MarkSerializer(mark)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = MarkSerializer(mark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        mark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def api_mark_models(request, mark_pk):
    """API представление Моделей автомобилей определенной Марки"""
    if request.method == 'GET':
        models = Model.objects.filter(mark=mark_pk)
        serializer = ModelSerializer(models, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def api_mark_model_detail(request, mark_pk, pk):
    """API представление одной Модели автомобилей"""
    model = Model.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ModelSerializer(model)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = ModelSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def api_orders(request):
    """API представление всех Заказов"""
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_order_detail(request, pk):
    """API представление одного заказа"""
    order = Order.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def api_shops(request):
    """API представление всех Магазинов"""
    if request.method == 'GET':
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_shop_detail(request, pk):
    """API представление одного магазина"""
    shop = Shop.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ShopSerializer(shop)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def api_answers(request):
    """API представление всех Ответов"""
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_answer_detail(request, pk):
    """API представление одного Ответа"""
    answer = Answer.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
