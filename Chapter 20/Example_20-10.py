from descriptorkinds import Managed

obj = Managed()

obj.over

Managed.over

obj.over = 7

obj.over

obj.__dict__['over'] = 8
vars(obj)

obj.over

obj.over_no_get

Managed.over_no_get

obj.over_no_get = 7

obj.over_no_get

obj.__dict__['over_no_get'] = 9

obj.over_no_get

obj.over_no_get = 7

obj.over_no_get
