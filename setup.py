# setup.py
from setuptools import setup, find_packages

setup(
    name='penelopa-dialog',
    version='0.0.1',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='Penelopa Dialog for managing and coordinating tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/penelopa-dialog',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
