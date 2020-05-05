from coroaverager0 import averager

coro_avg = averager()

next(coro_avg)

coro_avg.send(10)

coro_avg.send(30)

coro_avg.send(5)
