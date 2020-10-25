import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcexample",
    version="0.0.1",
    author="Ellie Hutcherson",
    description="A small example package for google cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Labgit/gcexample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)