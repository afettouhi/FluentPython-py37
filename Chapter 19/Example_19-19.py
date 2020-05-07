class Class:
    data = 'the class data attr'

    @property
    def prop(self):
        return 'the prop value'


obj = Class()
vars(obj)

obj.data

obj.data = 'bar'
vars(obj)

obj.data

Class.data

Class.prop

obj.prop

obj.prop = 'foo'

obj.__dict__['prop'] = 'foo'
vars(obj)

obj.prop

Class.prop = 'baz'
obj.prop

obj.data

Class.data

Class.data = property(lambda self: 'the "data" prop value')
obj.data

del Class.data
obj.data
