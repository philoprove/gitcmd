from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gitcmd',
    version='1.0.1',

    description='',
    long_description=long_description,

    url='https://github.com/philoprove/gitcmd',

    author='Kenny Zhang',
    author_email='sphy@foxmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: CVS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],

    keywords='git gitlab github',
    packages=['gitcmd'],

    install_requires=['pexpect'],
)
