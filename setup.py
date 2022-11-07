# This file describes the package for publication in the PyPI

from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="snake",
    version="0.1.0",
    description="Creating snake with Python, how ironic?",
    long_description=readme,
    author="Majestic Dreamers",
    url="https://github.com/AGH-Narzedzia-Informatyczne-2022-2023/majestic-dreamers",
    license=license,
    packages=find_packages(),  # Those so called "packages" really are second level modules
    entry_points={
        "console_scripts": [
            "snake=snake.main:main",
        ]
    },
)
