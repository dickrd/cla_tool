from distutils.core import setup

from setuptools import find_packages

setup(
    name='cla_tool',
    version='1.0.0',
    packages=find_packages(exclude=['res']),
    url='',
    license='MIT',
    author='DickRD',
    author_email='dickdata7@gmail.com',
    description='Chinese language analyze tools.',
    scripts=['bin/claserver'],
    install_requires=['gensim', 'jieba', 'sklearn', 'drest'],
    test_requires=['pytest'],
    test_suit="pytest"
)
