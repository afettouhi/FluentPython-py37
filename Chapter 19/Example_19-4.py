from osconfeed import load
from explore0 import FrozenJSON

raw_feed = load()
feed = FrozenJSON(raw_feed)

len(feed.Schedule.speakers)

sorted(feed.Schedule.keys())

for key, value in sorted(feed.Schedule.items()):
    print('{:3} {}'.format(len(value), key))

feed.Schedule.speakers[-1].name

talk = feed.Schedule.events[40]
type(talk)

talk.name

talk.flavor
