from io import open as io_open
import os

from setuptools import find_packages, setup

dirname = os.path.dirname(__file__)
readme_file = os.path.join(dirname, "README.md")
if os.path.exists(readme_file):
    with io_open(readme_file, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    # When this is first installed in development Docker, README.md is not available
    long_description = ""

# major, minor, patch
version_info = 0, 4, 3
# Nice string for the version
__version__ = ".".join(map(str, version_info))

setup(
    name="localtileserver",
    version=__version__,
    description="Locally serve geospatial raster tiles in the Slippy Map standard.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bane Sullivan",
    author_email="banesullivan@gmail.com",
    url="https://github.com/banesullivan/localtileserver",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click",
        "flask>=2.0.0",
        "Flask-Caching",
        "flask-restx>=0.5.0",
        "GDAL",
        "large-image>=1.10",
        "large-image-source-gdal>=1.10",
        "requests",
        "scooby",
    ],
    extras_require={
        "colormaps": ["matplotlib", "colorcet", "cmocean"],
        "sources": ["large-image-source-pil>=1.10", "large-image-source-tiff>=1.10"],
        "jupyter": ["jupyter-server-proxy", "ipyleaflet", "folium"],
    },
    entry_points={
        "console_scripts": [
            "localtileserver = localtileserver.__main__:run_app",
        ],
    },
)
