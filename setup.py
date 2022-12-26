import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nepse-data",
    version="0.0.1",
    author="Keshav Khanal",
    author_email="me.keskhanal@gmail.com",
    description="a python package for getting price history of companies listed in nepse",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keskhanal/nepse-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)