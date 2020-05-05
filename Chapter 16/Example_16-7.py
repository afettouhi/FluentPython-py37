from coroaverager1 import averager
coro_avg = averager()
coro_avg.send(40)

coro_avg.send(50)

coro_avg.send('spam')

coro_avg.send(60)
