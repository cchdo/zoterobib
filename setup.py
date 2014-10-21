import os.path
from sys import version_info

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pyzotero',
    'django',
]


setup(
    name='zoterobib',
    version='1.0',
    description='zoterobib',
    long_description='Django app for zotero Simile Exhibit page',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='CCHDO',
    author_email='cchdo@ucsd.edu',
    url='',
    keywords='web wsgi',
    packages=['zoterobib'],
    include_package_data=True,
    install_requires=requires,
)
