import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chippermillet", # Replace with your own username
    version="0.0.1",
    author="Madhava-mng",
    author_email="alformint@gmail.com",
    description="Cryptography from madhava",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/chipperMillet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
