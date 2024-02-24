from setuptools import setup

""" I wanted to create a CLI-EntryPoint for the application. But I will not push. Just for the demonstration."""

setup(
    name="library",
    version="0.0.1",
    license="MIT",
    description="A simple library management system. Based on a Global AI Hub Python Bootcamp(Project Based).",
    author="Caner Tuncay",
    url="https://github.com/cnrtncy/library-globalaihub.git",
    keywords=["SIMPLE", "LIBRARY", "MANAGEMENT", "GLOBALAIHUB", "BOOTCAMP"],
    packages=["library"],
    entry_points={
        "console_scripts": [
            "library = library.app_entry:cli_entry_point",
        ]
    },
    install_requires=["rich"],
)
