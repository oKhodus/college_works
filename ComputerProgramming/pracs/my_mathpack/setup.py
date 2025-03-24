from setuptools import setup, find_packages

setup(
    name="mymath",
    version="0.1.0",
    packages=find_packages(),
    author="Oleksii (Alan) Khodus",
    author_email="exalchel@gmail.com",
    description="A math package with functions for solving quadratic equations and calculating the area of a circle",
    url="https://github.com/oKhodus/college_works",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)