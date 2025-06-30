from setuptools import setup, find_packages

setup(
    name="ifc2json",
    version="0.1.0",
    description="A tool to convert IFC files to JSON and back.",
    author="Jan Brouwer",
    author_email="jan@brewsky.nl",
    packages=find_packages(where="file_converters"),
    package_dir={"": "file_converters"},
    include_package_data=True,
    install_requires=["ifcopenshell","pandas"],
    python_requires=">=3.7",
)
