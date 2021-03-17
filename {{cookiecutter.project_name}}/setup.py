from pathlib import Path
from setuptools import setup, find_packages

with open(Path(__file__).resolve().parent / "README.md") as f:
    readme = f.read()

setup(
    name="{{cookiecutter.package_name}}",
    url="{{cookiecutter.url}}",
    author="{{cookiecutter.author}}",
    description="{{cookiecutter.description}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["{{cookiecutter.package_name}}"]),
    install_requires=[],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
