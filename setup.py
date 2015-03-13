from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='hub',
    version=version,
    description='ERPNext Commerce Hub',
    author='Frappe',
    author_email='info@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
