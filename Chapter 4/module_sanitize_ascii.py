"""Example 4-17"""

from module_sanitize_latin import *

single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)


def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)
