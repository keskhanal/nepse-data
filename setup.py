import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nepal-stock-price",
    version="0.0.1",
    author="Keshav Khanal",
    author_email="me.keskhanal@gmail.com",
    description="a python package for getting price history of companies listed in nepse",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keskhanal/nepse-data",
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4==4.11.1',
        'bs4==0.0.1',
        'Jinja2==3.1.2',
        'numpy==1.23.1',
        'pandas==1.4.3',
        'pycparser==2.21',
        'pywin32==304',
        'requests==2.28.1',
        'selenium==4.3.0',
        'urllib3==1.26.11',
        'webdriver-manager==3.8.3',
        'Werkzeug==2.2.1',
        'zipp==3.8.1',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)