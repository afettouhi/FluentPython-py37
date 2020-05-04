import decimal

ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1') / decimal.Decimal('3')
one_third

one_third == +one_third

ctx.prec = 28
one_third == +one_third

+one_third
