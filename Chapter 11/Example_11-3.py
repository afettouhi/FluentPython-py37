class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


f = Foo()
for i in f:
    print(i)

f[1]

20 in f

15 in f
