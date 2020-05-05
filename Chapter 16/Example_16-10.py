from coro_exc_demo import *
from inspect import getgeneratorstate

exc_coro = demo_exc_handling()
next(exc_coro)

exc_coro.send(11)

exc_coro.throw(DemoException)

getgeneratorstate(exc_coro)
