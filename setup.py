from setuptools import setup
from setuptools import find_packages

# or
# from distutils.core import setup
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='gen4id',  # 包名字
    version='1.0',  # 包版本
    description='This is a test of the setup',  # 简单描述
    author='tony-is-coding',  # 作者
    author_email='newbiwtan@163.com',  # 作者邮箱
    maintainer="tony-is-coing",
    packages=find_packages(),  # 包
    install_requires=[],
    long_description=long_description,
    classifiers=[  # 关于包的其他元数据(metadata)
        "Programming Language :: Python :: 3",  # 该软件包仅与Python3兼容
        "License :: OSI Approved :: MIT License",  # 根据MIT许可证开源
        "Operating System :: OS Independent",  # 与操作系统无关
    ],
)
