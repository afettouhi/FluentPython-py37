import unicodedata, functools

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
s1, s2

s1 == s2

nfc(s1) == nfc(s2)
