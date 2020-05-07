from descriptorkinds import Managed

obj = Managed()

obj.over

Managed.over

obj.over = 7

obj.over

obj.__dict__['over'] = 8
vars(obj)

obj.over
