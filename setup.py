# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools.command.develop import develop


requirements = [
    'Flask==0.12.4',
    'Flask-Bootstrap==3.3.7.1',
    'Flask-WTF==0.14.2',
    'dynaconf==0.5.2',
    'gunicorn==19.7.1',
    'import-string==0.1.0',
    'pymongo==3.5.1',
    'pyyaml>=4.2b1'
]

requirements_dev = [
    'pep8==1.7.0',
    'flake8==3.4.1',
    'pytest==3.2.3',
    'ipython==6.2.1',
    'Flask-DebugToolbar==0.10.1'
]


class PostDevelopCommand(develop):
    def run(self):
        command = f'pip install {" ".join(requirements_dev)}'
        os.system(command)
        develop.run(self)


setup(
    name='meucandidato',
    version='0.0.1',
    description='',
    author='Gilson Filho',
    author_email='me@gilsondev.in',
    url='https://github.com/meucandidato/meucandidato',
    packages=['meucandidato'],
    package_dir={'meucandidato': 'meucandidato'},
    entry_points={
        'console_scripts': ['mcand=meucandidato.cli:main']
    },
    cmdclass={
        'develop': PostDevelopCommand
    },
    include_package_data=True,
    install_requires=requirements
)
