from descriptorkinds import Managed

obj = Managed()

Managed.over = 1

Managed.over_no_get = 2
Managed.non_over = 3
obj.over, obj.over_no_get, obj.non_over
