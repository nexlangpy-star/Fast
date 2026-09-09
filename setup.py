from setuptools import setup, find_packages
import os

setup(
    name="Fast",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="devil",
    description="Fix Slow Tools",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_data={
        'Fast': ['*.so', 'python4'],
    },
    include_package_data=True,
    data_files=[
        ('lib', ["Fast/Fast.cpython-313.so"]),
    ],
    zip_safe=False,
)