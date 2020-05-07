from method_is_descriptor import Text

word = Text('forward')
word

word.reverse()

Text.reverse(Text('backward'))

Text('drawkcab')
type(Text.reverse), type(word.reverse)

list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')]))

Text.reverse.__get__(word)

Text.reverse.__get__(None, Text)

word.reverse

word.reverse.__self__

word.reverse.__func__ is Text.reverse
