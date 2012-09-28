from setuptools import setup, find_packages

setup(
    name             = 'Python, the weird bits!',
    version          = '0.0.0',
    description      = '''
    A walk down some of the slightly stranger alleys of our platform
    to discover corner cases and pitfalls that you never knew existed.
    ''',
    author           = 'Saager @dexterous Mhatre',
    author_email     = 'saager.mhatre@gmail.com',
    url              = 'https://github.com/dexterous/python-the-weird-bits',
    setup_requires   = ['vim', 'solarized'],
    install_requires = ['open-mind', 'sense-of-humour'],
    zip_safe         = False,
)
