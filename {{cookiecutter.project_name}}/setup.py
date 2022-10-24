from pathlib import Path

from setuptools import find_packages, setup
from extreqs import parse_requirements_files

with open(Path(__file__).resolve().parent / "README.md") as f:
    readme = f.read()

install_requires, extras_require = parse_requirements_files(
    Path(__file__).resolve().parent / "requirements.txt"
)

setup(
    name="{{cookiecutter.package_name}}",
    url="{{cookiecutter.url}}",
    author="{{cookiecutter.author}}",
    description="{{cookiecutter.description}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        include=["{{cookiecutter.package_name}}*"]
    ),
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">=3.9, <4.0",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
