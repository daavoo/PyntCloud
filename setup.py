from setuptools import setup, find_packages

# Version
MAJOR = 0
MINOR = 1
MICRO = 0

version = "{}.{}.{}".format(MAJOR, MINOR, MICRO)

setup(
    name='pyntcloud',
    version=version,
    description='Python library for working with 3D point clouds.',
    url='https://github.com/daavoo/pyntcloud',
    author='David de la Iglesia Castro',
    author_email='daviddelaiglesiacastro@gmail.com',
    license='HAKUNA MATATA',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "ipython",
        "matplotlib",
        "numba",
        "laspy"
    ],
)
