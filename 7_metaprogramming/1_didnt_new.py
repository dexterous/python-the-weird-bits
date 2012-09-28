class Foo(object):
    @staticmethod #not necessary
    def __new__(cls):
        return 'hello'

foo = Foo()

print type(foo), foo, repr(foo)
