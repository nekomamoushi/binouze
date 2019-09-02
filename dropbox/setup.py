
import sys
from setuptools import setup, find_packages

DEPENDENCIES = ["dropbox"]

if sys.version_info[0] == 2:
    DEPENDENCIES.append("pathlib2")

setup(
    name='droopy',
    version='0.1.0',
    description='upload files to dropbox',
    author='Nekomamoushi',
    author_email='nekomamoushi@github.com',
    license='MIT',
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    zip_safe=False,
    entry_points={
        'console_scripts': ['droopy = droopy:main']
    }
)
