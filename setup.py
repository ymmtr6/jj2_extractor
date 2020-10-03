import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="jj2_extractor",
    version="0.0.1",
    author="riku yamamoto",
    author_email="ymmtr6@gmail.com",
    description="for JJ2, Informatics, Kindai Univ.",
    long_description=long_description,
    url="https://github.com/ymmtr6/jj2_extractor",
    pakages=setuptools.find_packages(),
    classifiers=[
        "Programinng Language :: Python :: 3",
        "Lisence :: MIT Lisence",
        "Operationg System :: OS Independent"
    ],
    entry_points={
        "console_scripts": ["jj2_extractor = jj2.jj2_extractor:main"]
    },
    python_requires=">=3.5"
)
