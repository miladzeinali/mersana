from django.shortcuts import render


def OrderControl(self, request):
    user = request.user
    data = request.data
    code = data['code']
    qty = data['qty']
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        if product.count != 0 and product.count >= qty:
            price = product.price
            if product.Sale == True:
                price = product.sale_price
            try:
                orderitem = OrderItem.objects.get(order=order, product=product)
                if product.count > orderitem.quantity:
                    orderitem.quantity += qty
                    orderitem.save()
                else:
                    return Response({'orderItem Maxmized'}, status.HTTP_400_BAD_REQUEST)
            except:
                OrderItem.objects.create(order=order, product=product,
                                         quantity=qty, price=price)
            resp = ('product Added',)
            return Response(resp, status=status.HTTP_200_OK)
        else:
            resp = ('product sold Out',)
            return Response(resp, status=status.HTTP_404_NOT_FOUND)
    except:
        order = Order.objects.create(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        if product.count != 0 and product.count >= qty:
            OrderItem.objects.create(order=order, product=product, quantity=qty)
            return Response(('product Added!',), status=status.HTTP_200_OK)
        else:
            order.delete()
            return Response(('product sold Out',), status=status.HTTP_404_NOT_FOUND)


def OrderItemChange(self, request):
    user = request.user
    code = request.data['code']
    qty = request.data['qty']
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        orderitem = OrderItem.objects.get(order=order, product=product)
        if orderitem.quantity == 1 and qty < 1:
            orderitem.delete()
            try:
                OrderItem.objects.get(order=order)
            except:
                order.delete()
            return Response({'product deleted'}, status=status.HTTP_200_OK)
        if product.count > orderitem.quantity:
            orderitem.quantity += qty
            orderitem.save()
            if orderitem.quantity == '0':
                orderitem.delete({'orderitem deleted'}, status.HTTP_200_OK)
                return Response()
            return Response({'orderItem Maxmized'}, status.HTTP_400_BAD_REQUEST)
        return Response({'OrderItem modified'}, status=status.HTTP_200_OK)
    except:
        return Response({'error in modifing Order Item'}, status=status.HTTP_304_NOT_MODIFIED)


def OrderItemDelete(self, request):
    user = request.user
    code = request.data['code']
    try:
        order = Order.objects.get(user=user, status='Wpay')
        product = Product.objects.get(code=code)
        orderitem = OrderItem.objects.get(order=order, product=product)
        orderitem.delete()
        product.count += orderitem.quantity
        return Response({'OrderItem Deleted'}, status=status.HTTP_200_OK)
    except:
        return Response({'error in OrderItem Deleting'}, status=status.HTTP_304_NOT_MODIFIED)
