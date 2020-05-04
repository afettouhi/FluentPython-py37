import itertools

list(itertools.groupby('LLLLAAGGG'))

for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
           'bat', 'dolphin', 'shark', 'lion']

animals.sort(key=len)
animals

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
