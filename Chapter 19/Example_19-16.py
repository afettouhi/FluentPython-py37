from bulkfood_v1 import LineItem

raisins = LineItem('Golden raisins', 10, 6.95)
raisins.subtotal()

raisins.weight = -20  # garbage in...
raisins.subtotal()  # garbage out...
