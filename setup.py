from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Project Module package',
    long_description=readme,
    author='tesisgeneracion2110',
    author_email='fonseca.oscar@javeriana.edu.co',
    url='https://github.com/tesisgeneracion2110/lyrics-module',
    license=license_file,
    install_requires=[
        'pytest'
    ],
    packages=find_packages(exclude=('tests', 'docs'))
)
