import json
from product.models import Product
import uuid


def product_already_exists(product_name, product_id):
    """
    Method: Check if a product with the given name already exists in the database.

    Args:
        product_name (str): Product name.

    Returns:
        True if the same product name already present in the database, else False.
    """
    try:
        if product_id:
            return Product.objects.filter(product_name__iexact=product_name).exclude(id=uuid.UUID(product_id).hex).exists()
        else:
            return Product.objects.filter(product_name__iexact=product_name).exists()
    except Exception:
        return True


def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product
    except Product.DoesNotExist:
        return None

def get_product_by_old_id(old_id):
    try:
        product = Product.objects.get(old_id=old_id)
        return product
    except Product.DoesNotExist:
        return None
    
def get_product_code():
    count = Product.objects.filter(product_code__isnull=False).count() + 7
    triple_digit_number = '{:03d}'.format(count)
    product_code = "PC"+triple_digit_number
    product_code_object = Product.objects.filter(product_code=product_code).first()
    if product_code_object:
        product_code = None
    return product_code

def get_product_by_sku(sku):
    try:
        product = Product.objects.filter(sku=sku).first()
        return product
    except Product.DoesNotExist:
        return None

def get_product_by_code(code):
    try:
        product = Product.objects.filter(product_code=code).first()
        return product
    except Product.DoesNotExist:
        return None