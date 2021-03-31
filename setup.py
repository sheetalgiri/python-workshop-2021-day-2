from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python tutorial',
    version='0.1.0',
    description='python tutorial for Team Saathi',
    long_description=readme,
    author='Sheetal Giri',
    packages=find_packages(exclude=('tests', 'docs'))
)
