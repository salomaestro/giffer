from setuptools import setup, find_packages

VERSION = "0.1.2"
DESCRIPTION = "Basic .gif converter"

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="giffer",
    version=VERSION,
    author="Salomaestro",
    author_email="<chris10an.salomonsen@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/salomaestro/giffer",
    packages=find_packages(),
    install_requires=["imageio", "numpy", "Pillow"],
    keywords=["python", "basic", "gif"],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X"
    ]
)