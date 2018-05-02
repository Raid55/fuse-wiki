import os

from setuptools import setup, find_packages


requires = [
    'Flask',
    'sqlite3',
    'requests',
    'flask_cors'
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

flask-cors == 3.0.3
google-cloud-logging == 1.5.0
google-compute-engine == 2.7.6
gunicorn == 19.7.1
requests == 2.18.4
supervisor == 3.3.4
