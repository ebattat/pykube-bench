from codecs import open
from os import path
from setuptools import setup, find_packages

__version__ = '1.0.0'
here = path.abspath(path.dirname(__file__))


if path.isfile(path.join(here, 'README.md')):
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = ""


setup(
    name='pykube-bench',
    version=__version__,
    description='Automate Benchmark Framework',
    long_description=long_description,
    author='Red Hat',
    author_email='ebattat@redhat.com',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],

    zip_safe=False,

    # Find all packages (__init__.py)
    packages=find_packages(include=['pykube_bench', 'pykube_bench.*']),

    install_requires=[
        'typing',
        'elasticsearch'

    ],

    setup_requires=['pytest-runner', 'wheel'],

    include_package_data=True,

    # dependency_links=[]

)
