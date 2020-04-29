"""Example 6-6"""

from order_discount import *

promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    """
    Select best discount available
    """
    return max(promo(order) for promo in promos)
