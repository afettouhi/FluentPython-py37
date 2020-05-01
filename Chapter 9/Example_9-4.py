class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


Demo.klassmeth()

Demo.klassmeth('spam')

Demo.statmeth()

Demo.statmeth('spam')
