from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in furniture/__init__.py
from furniture import __version__ as version

setup(
	name="furniture",
	version=version,
	description="Furniture App",
	author="Jenan Alfahham",
	author_email="jenan_95@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
