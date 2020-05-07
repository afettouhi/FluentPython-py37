from descriptorkinds import Managed

obj = Managed()
obj.non_over

obj.non_over = 7
obj.non_over

Managed.non_over

del obj.non_over
obj.non_over
