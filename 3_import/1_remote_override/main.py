import greeter
from greeter import hello

print hello('World')         # => Hello, World!
print greeter.hello('World') # => Hello, World!

import poison

print hello('World')         # => Hello, World!
print greeter.hello('World') # => Bye, World!
