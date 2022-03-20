from setuptools import find_packages, setup

import httpy

tests_require = [
    "pytest",
]
dev_require = [
    *tests_require,
    "flake8",
    "pyyaml",
    "twine",
    "wheel",
]
install_requires = [
    "requests>=2.27.0",
    "Pygments>=2.5.2",
    "setuptools",
]

extras_require = {
    "dev": dev_require,
    "test": tests_require,
}


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="httpy",
    version=httpy.__version__,
    description="Modern, user-friendly, programmable command-line HTTP client for the API.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author=httpy.__author__,
    author_email="sinan_kanidagli@hotmail.com",
    license=httpy.__licence__,
    packages=find_packages(include=["httpy", "httpy.*"]),
    entry_points={
        "console_scripts": [
            "httpy = httpy.__main__:main",
        ],
    },
    python_requires=">=3.7",
    extras_require=extras_require,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: System :: Networking",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    project_urls={
        "GitHub": "https://github.com/SinanKanidagli/httpy",
        "Twitter": "https://twitter.com/KanidagliV",
        "Documentation": "https://github.com/SinanKanidagli/httpy/docs",
    },
)
