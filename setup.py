import re
from glob import glob
from os.path import basename
from os.path import splitext
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def read(file):
    with (Path(__file__).parent / file).open() as fd:
        return fd.read()


setup(
    name='ttracker',
    description='Timetracker for idiots',
    license='GPLv2',
    use_scm_version=True,
    long_description='%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
    ),
    author='Marian Beermann',
    author_email='public+tt@enkore.de',
    url='https://github.com/enkore/tt',
    py_modules=['ttracker'],
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
    ],
    keywords=[
    ],
    setup_requires=['setuptools_scm>=1.7'],
    install_requires=[
    ],
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'tt-entry   = ttracker:entry',
            'tt-plot    = ttracker:plot',
        ],
    }
)
