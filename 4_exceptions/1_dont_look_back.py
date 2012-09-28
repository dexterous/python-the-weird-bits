import sys

try:
    raise
except:
    print sys.exc_info()[1], '\n'

try:
    raise 'foo'
except:
    print sys.exc_info()[1], '\n'
