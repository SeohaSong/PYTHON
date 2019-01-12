
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="shs",
    version="1.0.1",
    author="seohasong",
    author_email="tisutoo@gmail.com",
    description="SEOHASONG Packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SeohaSong/python-shs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
