import copy
from bus import Bus

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
id(bus1), id(bus2), id(bus3)

bus1.drop('Bill')
bus2.passengers

id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)

bus3.passengers
