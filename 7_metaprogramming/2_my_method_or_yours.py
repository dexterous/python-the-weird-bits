class Foo(object): pass

import types as t
import sys

def a_method(self):
    return 'meta'

Foo.method_on_class = a_method
#Foo.method_on_class = t.UnboundMethodType(a_method, Foo)

foo = Foo()
foo.method_on_instance = t.MethodType(a_method, foo)

print Foo.method_on_class, Foo.method_on_class(foo)
print foo.method_on_class, foo.method_on_class()

print foo.method_on_instance, foo.method_on_instance()
