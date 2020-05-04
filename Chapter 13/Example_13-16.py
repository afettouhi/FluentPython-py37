from bingoaddable import AddableBingoCage

vowels = 'AEIOU'
globe = AddableBingoCage(vowels)
globe.inspect()

globe.pick() in vowels

len(globe.inspect())
globe2 = AddableBingoCage('XYZ')
globe3 = globe + globe2
len(globe3.inspect())

void = globe + [10, 20]
