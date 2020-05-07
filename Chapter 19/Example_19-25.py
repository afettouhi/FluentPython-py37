from bulkfood_v2prop import LineItem

nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
nutmeg.weight, nutmeg.price

sorted(vars(nutmeg).items())
