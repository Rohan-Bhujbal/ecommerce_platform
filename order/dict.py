from django.forms.models import model_to_dict
import json

def order_dict(order):
    order_dict = model_to_dict(order)
    order_dict['id'] = str(order.id)
    order_dict['total'] =  int(order.total)
    order_dict['user_id'] = str(order.user_id)
    order_dict['created_at'] = str(order.created_at)
    order_dict['updated_at'] = str(order.updated_at)
    if order.deleted_at:
        order_dict['deleted_at'] = str(order.deleted_at)
    return order_dict
