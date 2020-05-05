from taxi_sim import taxi_process
taxi = taxi_process(ident=13, trips=2, start_time=0)
next(taxi)

taxi.send(_.time + 7)

taxi.send(_.time + 23)

taxi.send(_.time + 5)

taxi.send(_.time + 48)

taxi.send(_.time + 1)

taxi.send(_.time + 10)
