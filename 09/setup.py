"""Module that provides 'pip install .' command available"""
from setuptools import Extension, setup

# Name here is the name of .so file: cjson.so
ext_module = Extension("cjson", ["cjson.c"])

# Name here is the name of package that we will install by pip and connect to our python script: pip install cjson
setup(
    name="cjson",
    version="1.0",
    description="Module which provides serialization and deserialization of JSON",
    ext_modules=[ext_module]
)
