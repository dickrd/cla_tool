from distutils.core import setup

from setuptools import find_packages

setup(
    name='cla_tool',
    version='1.0.0',
    packages=find_packages(exclude=['res']),
    url='https://github.com/dickrd/cla_tool',
    license='Apache License 2.0',
    author='DickRD',
    author_email='dickdata7@gmail.com',
    description='Chinese language analyze tools.',
    scripts=['bin/cla'],
    install_requires=['gensim', 'jieba', 'sklearn'],
    test_requires=['pytest'],
    test_suit="pytest"
)
