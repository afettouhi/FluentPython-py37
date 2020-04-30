from hauntedbus import HauntedBus

bus1 = HauntedBus(['Alice', 'Bill'])
bus1.passengers

bus1.pick('Charlie')
bus1.drop('Alice')
bus1.passengers

bus2 = HauntedBus()
bus2.pick('Carrie')
bus2.passengers

bus3 = HauntedBus()
bus3.passengers

bus3.pick('Dave')
bus2.passengers

bus2.passengers is bus3.passengers

bus1.passengers
