from setuptools import setup
from codecs import open
from os import path

from phonopasswd import __version__


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='phonopasswd',
    version=__version__,
    description='Phonetic passwords generator',
    long_description=long_description,
    url='https://github.com/andr1an/phonopasswd',
    author='Sergey Andrianov',
    author_email='info@andrian.ninja',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='password security tools',
    packages=['phonopasswd'],
    entry_points={
        'console_scripts': [
            'phonopasswd=phonopasswd:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/andr1an/phonopasswd/issues',
        'Source': 'https://github.com/andr1an/phonopasswd',
    },
)
