import weakref
from cheese import Cheese

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

sorted(stock.keys())

del catalog
sorted(stock.keys())

del cheese
sorted(stock.keys())
