from setuptools import setup, find_packages
import io
import os
import versioneer

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pandoctools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='Profile manager of text processing pipelines: Pandoc filters, any text CLI filters. Atom+Markdown+Pandoc+Jupyter workflow, export to ipynb.',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://github.com/kiwi0fruit/pandoctools',

    author='Peter Zagubisalo',
    author_email='peter.zagubisalo@gmail.com',

    license='GPLv2+',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    # keywords='sample setuptools development',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6',
    install_requires=['click', 'pyyaml', 'notebook', 'jupyter', 'libsass', 'shutilwhich-cwdpatch>=0.1.0',
                      'panflute>=1.11.2', 'knitty>=0.5.0', 'pyppdf>=0.0.10',
                      'sugartex>=0.1.16', 'shortcutter>=0.1.19', 'numpy',
                      'py-pandoc>=2.6', 'py-pandoc-crossref>=0.3.4.0.3', 'py-mathjax'],
    # click pyyaml notebook jupyter libsass "panflute>=1.11.2" "knitty>=0.5.0" "pyppdf>=0.0.10" "sugartex>=0.1.16" "shortcutter>=0.1.19" "numpy" "py-pandoc>=2.6" "py-pandoc-crossref>=0.3.4.0.3" py-mathjax "shutilwhich-cwdpatch>=0.1.0"

    include_package_data=True,
    entry_points={
        'console_scripts': [
            'cat-md=pandoctools.cat_md.cat_md:cli',
            'pandoctools=pandoctools.cli.cli:pandoctools',
            'pandoctools-resolve=pandoctools.pandoctools_resolve.resolve:cli',
            'pandoctools-ready=pandoctools.ready.ready:ready',
        ],
    },
)
