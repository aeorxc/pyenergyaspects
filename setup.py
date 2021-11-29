import setuptools

setuptools.setup(
    name="pyenergyaspects",
    version="0.0.1",
    author="aeorxc",
    description="Wrapper around Energy Aspects API",
    url="https://github.com/aeorxc/pyenergyaspects",
    project_urls={
        "Source": "https://github.com/aeorxc/pyenergyaspects",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "requests"],
    python_requires=">=3.8",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
