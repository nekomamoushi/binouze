
from setuptools import setup, find_packages


setup(
    name='droopy',
    version='0.1.0',
    description='upload files to dropbox',
    author='Nekomamoushi',
    author_email='nekomamoushi@github.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['dropbox'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['droopy = droopy:main']
    }
)
