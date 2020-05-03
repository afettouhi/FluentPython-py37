class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
dd

dd['two'] = 2
dd

dd.update(three=3)
dd
