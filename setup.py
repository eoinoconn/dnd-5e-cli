import setuptools

setuptools.setup(
    name="dnd-5e-cli",
    version="0.0.1",
    author="Eoin OConnell",
    author_email="eoinoconn@gmail.com",
    description="A simple DnD CLI tool.",
    url="https://github.com/eoinoconn/dnd-5e-cli",
    project_urls={
        "Bug Tracker": "https://github.com/eoinoconn/dnd-5e-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)