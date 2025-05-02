from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="arxiv-harvester",
    version="0.1.0",
    author="arxiv-harvester Contributors",
    description="A rate-limit-compliant OAI-PMH harvester for ArXiv papers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M-Chimiste/arxiv-harvester",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "pandas": ["pandas>=1.0.0"],
    }
) 
