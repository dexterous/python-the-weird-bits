import sys

print sys.exc_info()

try:
    raise BaseException
except:
    print sys.exc_info()

print sys.exc_info()
