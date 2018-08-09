import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dr',
    version='1.9.1',
    description='An ed-like devRant client',
    url='https://github.com/Ewpratten/dr',
    author='Evan Pratten',
    author_email='ewpratten@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["dr"],
    install_requires=['requests', 'classRant', 'devRantSimple'],
    entry_points={
        'console_scripts': ['dr = dr.dr:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
)
