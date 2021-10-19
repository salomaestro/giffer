from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Basic .gif converter"
LONG_DESCRIPTION = "A basic package which converts a folder of .png images to .gif file."

setup(
    name="giffer",
    version=VERSION,
    author="Salomaestro",
    author_email="<chris10an.salomonsen@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["imageio", "numpy", "Pillow"],
    keywords=["python", "basic", "gif"],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X"
    ]
)