import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
DESCRIPTION = "slugrn"

PKGS = find_packages()
PKG_NAME = "slugrn"
PKG_VERSION = '1.0.1'

MAINTAINER = 'Zac Reeves'
MAINTAINER_EMAIL = '129307974+archzaq@users.noreply.github.com'

PYTHON_REQUIRES = ">=3.8"
URL = "https://github.com/archzaq/SLU_QuantumGRN"

LICENSE = "MIT"
CLFS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
]

INSTALL_REQUIRES = [
    "numpy>=1.23.0",
    "matplotlib>=3.5.2",
    "pandas>=1.4.3",
    "scipy>=1.8.1",
    "qiskit>=0.37.0",
    "qiskit-aer>=0.10.4",
    "igraph>=0.9.11",
    "Pillow>=9.2.0",
    "requests>=2.28.1",
    "pylatexenc>=2.10",
    "cairocffi>=1.7.1",
    "pycairo>=1.21.0",
]

# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=PKG_VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    author=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    license=LICENSE,
    classifiers=CLFS,
    packages=PKGS,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    # entry_points={
    #     "console_scripts": [
    #         "scTenifold=scTenifold.__main__:app",
    #     ]
    # },
)
