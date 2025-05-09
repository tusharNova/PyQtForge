from setuptools import setup , find_packages


setup(
    name = "pyqtforge",
    version="0.1.7",
    package = find_packages(),
    include_package_data=True,
    install_requires=[
        "typer",
        "click",
        "uv",
        "pyqt5",
        "pyqt5-tools"
    ],
    entry_points={
    "console_scripts": [
        "pyqtforge=pyqtforge.cli:main"
    ]
},
    author = "Tushar Mankar",
    description="A CLI tool to scaffold and manage PyQt projects easily.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url = "https://github.com/tusharNova/PyQtForge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",

)

