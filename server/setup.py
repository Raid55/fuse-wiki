import os

from setuptools import setup, find_packages


requires = [
    'Flask',
    'sqlite3',
    'requests',
    'flask_cors',
    'gunicorn',
    'supervisor'
]


setup(
    name='fuse.wiki-server',
    version='0.5',
    description='6 degrees of wikipedia',
    author='David Yoon, Sid Carroll, Jay Biehler, Jacob Hartman, Nicholas Boutboul',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires
)
