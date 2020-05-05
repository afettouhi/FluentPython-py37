from mirror import LookingGlass
manager = LookingGlass()

manager

monster = manager.__enter__()
monster == 'JABBERWOCKY'


monster

manager

manager.__exit__(None, None, None)
monster
