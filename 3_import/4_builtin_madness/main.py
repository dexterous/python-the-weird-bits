#!/usr/bin/env python

# if...

__builtins__.open = 'foo'

# ... is allowed yet results in...

print __builtins__.open #=> <built-in function open>

# ... then why is...

__builtins__.None = 'bar'

# ... a SyntaxError?
