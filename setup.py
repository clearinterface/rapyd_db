import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sql_bootstrap',
    version='0.0.2',
    description='An opinionated lightweight wrapper around various SQL backend drivers.',
    long_description=readme,
    author='Karthic Raghupathi',
    author_email='karthicr@gmail.com',
    url='https://github.com/karthicraghupathi/sql_bootstrap',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    extras_require={
        'mysql': [
            'mysqlclient'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)