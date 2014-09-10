from setuptools import setup

desc = 'piptesta'
setup(
    name='piptesta',
    description=desc,
    packages=['piptesta'],
    install_requires=['piptestb==dev'],
    dependency_links=[
        'git+ssh://git@github.com/c-oreills/piptestb.git@9ff93995a260f3eafdecc57b3e3377a378692d36#egg=piptestb-dev'
    ],
    long_description=desc,
)
