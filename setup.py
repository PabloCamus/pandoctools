from setuptools import setup, find_packages
from setuptools.command.install import install

import os
import versioneer

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pandoctools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='Pandoc profile manager (stores any CLI filter pipelines), CLI wrapper for Panflute, other helpers.',
    long_description=long_description,

    url='https://github.com/kiwi0fruit/pandoctools',

    author='Peter Zagubisalo',
    author_email='peter.zagubisalo@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # keywords='sample setuptools development',
    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=['click', 'pyyaml', 'panflute', 'knitty>=0.3.10', 'pandas',
                      'sugartex>=0.1.9', 'matplotlib', 'feather-format',  # 'shortcut',
                      'notebook', 'jupyter', 'winshell;platform_system=="Windows"',
                      'pywin32;platform_system=="Windows"'],

    include_package_data=True,
    package_data={
        'pandoctools': ['bat/*', 'sh/*'],
    },
    entry_points={
        'console_scripts': [
            'cat-md=pandoctools.cat_md.cat_md:cat_md',
            'pandoctools=pandoctools.cli.cli:pandoctools',
            'panfl=pandoctools.panfl.panfl:main',
        ],
    },
    scripts=[
        'scripts/pandoc19_fix_html_indent.py',
        'scripts/pandoctools-import',
        'scripts/pandoctools-import.bat',
        'scripts/pandoctools-resolve',
        'scripts/pandoctools-resolve.bat',
        'scripts/path-run.bat',
        'scripts/path-source',
        'scripts/path-source.bat',
        'scripts/path-pyprep',
        'scripts/path-pyprep-win',
        'scripts/path-pyprep.bat',
        'scripts/setvar.bat',
        'scripts/pandoctools-cygpath',
    ],
)
