"""Example 7-9, 10, 11 & 12"""


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


avg = make_averager()
avg(10)

avg(11)

avg(12)

avg.__code__.co_varnames

avg.__code__.co_freevars

avg.__code__.co_freevars

avg.__closure__

avg.__closure__[0].cell_contents
