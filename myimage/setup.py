from setuptools import setup, find_packages

setup(
    name="myimage",
    version="0.1",
    description="A simple wrapper around Pillow for image manipulation",
    author="Jithu",
    packages=find_packages(),
    install_requires=["Pillow"],
    python_requires=">=3.6",
)
