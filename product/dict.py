from django.forms.models import model_to_dict

def product_dict(product):
    product_dict = model_to_dict(product)
    product_dict['product_image'] = product.product_image
    product_dict['id'] = str(product.id)
    product_dict['author'] = str(product.author)
    product_dict['created_at'] = str(product.created_at)
    product_dict['updated_at'] = str(product.updated_at)
    if product.deleted_at:
        product_dict['deleted_at'] = str(product.deleted_at)
    return product_dict
