import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='flare',
      version='1.0',
      description='eer test tool',
      long_description=long_description(),
      url='https://github.com/s10cho/flare-py-1.1',
      author='s10cho',
      author_email='',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)