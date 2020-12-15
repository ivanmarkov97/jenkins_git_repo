import os
from setuptools import setup, find_packages

import calculator


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='calculator',
    version=calculator.__version__,
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
