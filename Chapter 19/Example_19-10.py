from schedule2 import *

DbRecord.set_db(db)
event = DbRecord.fetch('event.33950')
event

event.venue

event.venue.name

for spkr in event.speakers:
    print('{0.serial}: {0.name}'.format(spkr))
