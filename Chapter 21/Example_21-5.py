from bulkfood_v6 import LineItem

raisins = LineItem('Golden raisins', 10, 6.95)
dir(raisins)[:3]

LineItem.description.storage_name

raisins.description

getattr(raisins, '_NonBlank#description')
