colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
 ('white', 'M'), ('white', 'L')]
for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes
           for color in colors]
tshirts
