from setuptools import setup, find_packages

setup(
    name="ia-productiva",
    version="0.1.0",
    description="Framework per a desenvolupament assistit per IA amb memòria de context",
    author="Eduard Casellas",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ia-productiva = ia_productiva.cli:main",
        ],
    },
    python_requires=">=3.8",
)