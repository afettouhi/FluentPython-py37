from bingoaddable import AddableBingoCage

vowels = 'AEIOU'
globe = AddableBingoCage(vowels)
globe2 = AddableBingoCage('XYZ')
globe_orig = globe
len(globe.inspect())

globe += globe2
len(globe.inspect())

globe += ['M', 'N']
len(globe.inspect())

globe is globe_orig

globe += 1
