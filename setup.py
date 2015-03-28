"""
Package install setup script.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name ="crange",
    version = "0.1.2",
    description = "Crange is a tool to index and cross-reference C/C++ source code.",
    keywords = "crange, clang, llvm, parser, index, cross-reference, xref",
    author = "Anurag Patel",
    author_email = "gnurag@gmail.com",
    url = "https://github.com/crange/crange",
    download_url = 'https://github.com/crange/crange/releases',
    license = "BSD",
    packages = [
        "crange"
    ],
    scripts = [
        "crange/bin/crange",
        "crange/bin/crtags"
    ],
    install_requires = [
        "clang>=3.5",
        "tabulate>=0.7"
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2'
    ],
    test_suite = "test.py",
    tests_require = [
        "mock"
    ],
    long_description = """
Crange is a tool to index and cross-reference C/C++ source code. It
can be used to generate tags database that can help with:

* Identifier definitions
* Identifier declaraions
* References
* Expressions
* Operators
* Symbols
* Source range

The source metadata collected by Crange can help with building tools
to provide cross-referencing, syntax highlighting, code folding and
deep source code search.
    """
)
