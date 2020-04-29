from tag import tag
from functools import partial

tag

picture = partial(tag, 'img', cls='pic-frame')
picture(src='wumpus.jpeg')

picture

picture.func

picture.args

picture.keywords
