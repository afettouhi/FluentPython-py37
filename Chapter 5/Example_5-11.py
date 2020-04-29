from tag import *

tag('br')

tag('p', 'hello')

print(tag('p', 'hello', 'world'))

tag('p', 'hello', id=33)

print(tag('p', 'hello', 'world', cls='sidebar'))

tag(content='testing', name="img")

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
tag(**my_tag)
