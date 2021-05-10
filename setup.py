import setuptools

with open("README.md", "r") as f:
    readme = f.read()

setuptools.setup(
    name="saygeek",
    version="1.1.0",
    description="ALMA historical phrase generator",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jose L. Ortiz",
    author_email='jlortiz@uc.cl',
    url="https://github.com/bandaangosta/saygeek",
    packages=["saygeek"],
    package_data={"saygeek": ["resources/*"]},
    entry_points={
        "console_scripts": [
            "saygeek=saygeek.__main__:main"
        ],
    },
    license="MIT",
    install_requires=[
        "click==7.1.2",
        "typer==0.3.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)