symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii
