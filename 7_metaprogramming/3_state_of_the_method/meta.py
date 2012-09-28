import sys

class A(object):
    def a_method(self):
        pass

    print a_method
    print a_method.__module__

    print dir(sys.modules[__name__])

print A.a_method
print A.__dict__['a_method']
print A.a_method.__func__

print dir(sys.modules[__name__])
