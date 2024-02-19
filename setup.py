from setuptools import setup

""" I wanted to create a CLI-EntryPoint for the application. But I will not push. Just for the demonstration."""

setup(
    name="library-globalaihub",
    version="0.0.1",
    description="A simple library management system. Based on a Global AI Hub Python Bootcamp(Project Based).",
    author="Caner Tuncay",
    packages=["library"],
    entry_points={
        "console_scripts": [
            "library = library.app_entry:cli_entry_point",
        ]
    },
    install_requires=["rich", "setuptools"],
)
