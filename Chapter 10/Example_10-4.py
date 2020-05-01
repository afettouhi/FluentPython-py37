class MySeq:
    def __getitem__(self, index):
        return index


s = MySeq()
s[1]

s[1:4]

s[1:4:2]

s[1:4:2, 9]

s[1:4:2, 7:9]
