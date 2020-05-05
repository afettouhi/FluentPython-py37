from coro_exc_demo import *
from inspect import getgeneratorstate

exc_coro = demo_exc_handling()
next(exc_coro)

exc_coro.send(11)

exc_coro.send(22)

exc_coro.close()

getgeneratorstate(exc_coro)
