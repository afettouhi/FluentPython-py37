from tombola import Tombola


class Fake(Tombola):
    def pick(self):
        return 13


Fake

f = Fake()
