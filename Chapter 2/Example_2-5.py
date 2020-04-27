import array

symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)

array.array('I', (ord(symbol) for symbol in symbols))
