"""
Package install setup script.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="crange",
    version="0.0.1",
    description="Crange is a tool to index and cross-reference C/C++ source code.",
    keywords="crange, clang, llvm, parser, index, cross-reference, xref",
    author="Anurag Patel",
    author_email="gnurag@gmail.com",
    url="https://github.com/crange/crange",
    license="BSD",
    packages=[
        "crange"
    ],
    scripts=[
        "crange",
        "crtags"
    ],
    install_requires=[
        "clang",
        "sqlite3",
        "tabulate"
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2'
    ],
    test_suite="test.py",
    tests_require=[
        "mock"
    ]
)
