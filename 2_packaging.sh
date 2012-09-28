$python setup.py
$python setup.py sdist
$python setup.py bdist
$python setup.py bdist_egg
$python setup.py upload -r http://pypi.acme.org/simple
$#python setup.py upload -r http://username:password@pypi.acme.org/simple
$python setup.py upload -r acme

$easy_install foo.egg
$easy_install foo==0.0.1
$easy_install --index-url http://pypi.acme.org/simple foo==0.0.1

$pip install foo==0.0.1
$pip uninstall foo
$pip freeze
