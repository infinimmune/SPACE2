from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='clustruc',
    version='0.0.1',
    description='Set of functions to cluster CDR structures',
    license='BSD 3-clause license',
    maintainer='Brennan Abanades',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer_email='brennan.abanadeskenyon@stx.ox.ac.uk',
    include_package_data=True,
    packages=find_packages(include=('clustruc', 'clustruc.*')),
    install_requires=[
        'numpy>=1.20.0',
        'numba>=0.51.0',
        'joblib>=1.0.0',
        'pandas',
    ],
)