import shelve
from schedule1 import *

db = shelve.open(DB_NAME)

if CONFERENCE not in db:
    load_db(db)

speaker = db['speaker.3471']

type(speaker)

speaker.name, speaker.twitter

db.close()
