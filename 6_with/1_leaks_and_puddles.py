import contextlib as ctx

@ctx.contextmanager
def barman():
    yield 'goodbye'

drink = 'hello'

print drink

with barman() as drink:
    print drink

print drink
