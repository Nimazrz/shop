from django import template
from shop.models import Product

register = template.Library()
@register.inclusion_tag('partials/similar_post.html')
def similar_products(count:4, category_id, product_id):
    similar_products = Product.objects.filter(category=category_id).exclude(id=product_id)[:count]
    return {'similar_products':similar_products}