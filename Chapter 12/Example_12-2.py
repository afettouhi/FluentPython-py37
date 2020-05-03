class AnswerDict(dict):
    def __getitem__(self, key):
        return 42


ad = AnswerDict(a='foo')
ad['a']

d = {}
d.update(ad)
d['a']

d
