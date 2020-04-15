import os

from setuptools import setup
from setuptools import find_packages

# or
# from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()

except IOError:
    README = CHANGES = ''

setup(
    name='gen4id',  # 包名字
    version='1.0.2',  # 包版本
    description='gen4id a simple but maybe useful package for auto-increment ids ',  # 简单描述
    author='tony-is-coding',  # 作者
    author_email='newbiwtan@163.com',  # 作者邮箱
    maintainer="tony-is-coing",
    packages=find_packages(),  # 包
    install_requires=[],
    long_description=README,
    classifiers=[  # 关于包的其他元数据(metadata)
        "Programming Language :: Python :: 3",  # 该软件包仅与Python3兼容
        "License :: OSI Approved :: MIT License",  # 根据MIT许可证开源
        "Operating System :: OS Independent",  # 与操作系统无关
    ],
)
