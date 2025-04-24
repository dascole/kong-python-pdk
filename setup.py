#!/usr/bin/env python3
import os
import importlib.util
from setuptools import setup

PROJ_NAME = 'kong-pdk'
PACKAGE_NAME = 'kong_pdk'

here = os.path.abspath(os.path.dirname(__file__))

# Read project files
def read_file(filename):
    try:
        return open(os.path.join(here, filename)).read()
    except Exception:
        return ""

README = read_file('README.md')
CHANGELOG = read_file('CHANGELOG.md')

const_path = os.path.join(here, f'{PACKAGE_NAME}/const.py')
spec = importlib.util.spec_from_file_location('version', const_path)
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)

VERSION = version_module.__version__

packages = [
    'kong_pdk',
    'kong_pdk/pdk',
    'kong_pdk/pdk/kong',
    'kong_pdk/pdk/kong/client',
    'kong_pdk/pdk/kong/ctx',
    'kong_pdk/pdk/kong/nginx',
    'kong_pdk/pdk/kong/service',
    'kong_pdk/pdk/kong/enterprise_edition',
]
requires = ['gevent', 'msgpack']

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description='Kong PDK for Python and Plugin Server',
    long_description=README + '\n\n' + CHANGELOG,
    long_description_content_type="text/markdown",
    author='Kong',
    url='https://github.com/Kong/kong-python-pdk',
    packages=packages,
    package_dir={'requests': 'requests'},
    include_package_data=True,
    install_requires=requires,
    license="Apache-2.0",
    license_files=('LICENSE',),
    zip_safe=False,
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython'
    ),
    requires=requires,
    entry_points={'console_scripts': ["kong-python-pluginserver = kong_pdk.cli:start_server"]},
    package_data={"kong_pdk": ["*.pyi", "**/*.pyi", "**/**/*.pyi", "**/**/**/*.pyi"]}
)
