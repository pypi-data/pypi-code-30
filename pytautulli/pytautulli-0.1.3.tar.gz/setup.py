"""Setup configuration."""
import setuptools

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="pytautulli",
    version='0.1.3',
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description=LONG,
    install_requires=['requests', 'urllib3'],
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ludeeus/pytautulli",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
