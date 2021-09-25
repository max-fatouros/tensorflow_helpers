import setuptools

setuptools.setup(
    name="tensorflow_helper",
    version="0.0.1",
    author="Max Fatouros",
    description="helper methods for tensorflow",
    url="https://github.com/max-fatouros/tensorflow_helpers",

    package_dir={"": "tensorflow_helpers"},
    packages=setuptools.find_packages(where="tensorflow_helpers"),
    python_requires=">=3.6",
)
