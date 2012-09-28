class Hell(BaseException): pass

def raise_hell():
    raise Hell()

def absolve(func):
    try: func()
    except Hell:
        import sys, traceback
        traceback.print_exc(sys.exc_info())

def reraise_last():
    try: raise_hell()
    except Hell: raise

def catch_and_raise():
    try: raise_hell()
    except Hell as x: raise x

if __name__ == '__main__':
    absolve(reraise_last)
    absolve(catch_and_raise)
