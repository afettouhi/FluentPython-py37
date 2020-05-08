from record_factory import record_factory

Dog = record_factory('Dog', 'name weight owner')
rex = Dog('Rex', 30, 'Bob')
rex

name, weight, _ = rex

name, weight
"{2}'s dog weighs {1}kg".format(*rex)

rex.weight = 32

rex
Dog.__mro__
