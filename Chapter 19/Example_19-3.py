from osconfeed import load

feed = load()

sorted(feed['Schedule'].keys())

for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))

feed['Schedule']['speakers'][-1]['name']

feed['Schedule']['speakers'][-1]['serial']

feed['Schedule']['events'][40]['name']

feed['Schedule']['events'][40]['speakers']
