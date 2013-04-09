#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages  # NOQA
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        exit(errno)


setup(
    name='FormEncode-Jinja2',
    version='0.1.0',
    author='Eunchong Yu',
    author_email='kroisse@gmail.com',
    url='https://github.com/Kroisse/FormEncode-Jinja2',
    description='A Jinja2 extension for filling forms via FormEncode',
    license='MIT License',
    keywords='html',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'FormEncode',
        'Jinja2',
    ],
    extras_require={
        'doc': [
            'Sphinx',
        ],
    },
    tests_require=[
        'pytest',
    ],
    cmdclass={
        'test': PyTest,
    },
    dependency_links=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
