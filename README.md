# Pandoctools

Pandoctools is a combination of tools that help write reproducible markdown reports. They rely on Pandoc and Jupyter kernels.

**Introduction articles**:

* [**Best Python/Jupyter/PyCharm/VSCode experience + report generation with Pandoc filters**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/best_python_jupyter_pycharm_experience.md).
* [**Convenient and easily tweakable Atom+Markdown+Pandoc+Jupyter experience (can export to ipynb)**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/atom_jupyter_pandoc_markdown.md).  


“Glueing” part of pandoctools is a profile manager of text processing pipelines. It stores short crossplatform bash scripts that define chain operations over text. They are mostly Pandoc filters but any CLI text filter is OK.


## Update instructions

(*Update instructions to v.2.6*)

* **v2.6** is not backward compatible but profiles can be easily fixed. Uninstall Pandoctools before updating. Update your custom bash scripts as names and logic changed. References: [**Default_args**](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/sh/Default_args), [**Default**](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/sh/Default) (profile), [**Default_pipe**](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/sh/Default_pipe).


# Contents

* [Pandoctools](#pandoctools)
  * [Update instructions](#update-instructions)
* [Contents](#contents)
* [Notable parts of Pandoctools](#notable-parts-of-pandoctools)
* [Examples](#examples)
* [Install](#install)
* [Useful tips (reload imported modules in Hydrogen, Python kernel, R kernel, Typescript kernel)](#useful-tips-reload-imported-modules-in-hydrogen-python-kernel-r-kernel-typescript-kernel)
* [Alternatives to R Markdown (Markdown-based Literate Programming)](#alternatives-to-r-markdown-markdown-based-literate-programming)


# Notable parts of Pandoctools

* [**Pandoc**](https://pandoc.org/), [**Jupyter**](http://jupyter.org/), [**pandoc-crossref**](https://github.com/lierdakil/pandoc-crossref) (dependence) - classical tools.
* [**Pandoctools CLI app**](https://github.com/kiwi0fruit/pandoctools/tree/master/pandoctools/cli): profile manager of text processing pipelines. It stores short bash scripts - called profiles - that define chain operations over text. They are mostly Pandoc filters but any CLI text filter is OK. Profiles can be used to convert any document of choise in the specified manner.
* [**Knitty**](https://github.com/kiwi0fruit/knitty) (dependence): Jupyter power in plain Python/Julia/R/any-kernel-lang. Jupyter kernels output as Pandoc filter. Insert python code (or other Jupyter kernel code) to the Markdown document **or write in plain Python/Julia/R with block-commented Markdown** and have code's results in the output document. Stitch/Knotr fork: reproducible report generation tool via Jupyter, Pandoc and Markdown. Can export to .html, .pdf, [Jupyter .ipynb notebooks](https://pandoc.org/MANUAL.html#creating-jupyter-notebooks-with-pandoc) and any other [Pandoc output formats](https://pandoc.org/MANUAL.html#general-options). You can use [ipynb-py-convert](https://github.com/kiwi0fruit/ipynb-py-convert) to convert .ipynb to .py to use with Knitty.
* [**SugarTeX**](https://github.com/kiwi0fruit/sugartex) (dependence): SugarTeX is a more readable LaTeX language extension and transcompiler to LaTeX.
* [**Pyppdf**](https://github.com/kiwi0fruit/pyppdf) (dependence): Pyppeteer PDF. Prints html output to pdf via patched Pyppeteer.
* [**Prism.js**](https://github.com/PrismJS/prism) and [**github-markdown-css**](https://github.com/sindresorhus/github-markdown-css) (integrated): used for default to PDF conversion (but with borrowing from [Default_args](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/sh/Default_args) to custom profile you can use them with to HTML conversion too).
* [**libsass-python**](https://github.com/sass/libsass-python): tweak and write css with more convenient sass or scss (see [Default.sass](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/sh/Default.sass)). 
* (*optional*) [**Tabulate Helper**](https://github.com/kiwi0fruit/tabulatehelper) converts tabular data like Pandas dataframe to GitHub Flavored Markdown pipe table.
* (*optional*) [**Matplotlib Helper**](https://github.com/kiwi0fruit/matplotlibhelper): custom helper to tune Matplotlib experience in Atom/Hydrogen and Pandoctools/Knitty.
* (*optional*) [**Feather Helper**](https://github.com/kiwi0fruit/featherhelper): concise interface to cache numpy arrays and pandas dataframes.
* (*optional*) [**pypugjs**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/pug.md): Write HTML via Pug that is much more readable.

Pandoctools is a tool for converting markdown document. But we also need tools for writing markdown and deploying python/Jupyter code blocks.  
And the best one for it is:

* [**Atom editor with plugins**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/atom.md). It helps easily type Unicode, interactively run highlighed python/Jupyter code blocks and instantly see results (+ completions from the running Jupyter kernel), can convert basic pandoc markdown to html with live preview.
* Must have plugins: [**SugarTeX Completions**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/atom.md#sugartex-completions), [**Unix Filter**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/atom.md#unix-filter), [**Hydrogen**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/atom.md#hydrogen), [**Markdown Preview Plus**](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/atom.md#markdown-preview-plus)


# Examples

Here are [**examples**](https://github.com/kiwi0fruit/pandoctools/blob/master/examples) that demonstrate converting documents:

* from markdown `.md` with Jupyter python code blocks, SugarTeX math and cross-references to `.ipynb` notebook and to PDF.
* from Hydrogen/python notebook `.py` with Atom/Hydrogen code cells, Knitty markdown incerts (again with SugarTeX math and cross-references) to `.ipynb` notebook and to PDF.

**Examples are given for [to .ipynb](https://pandoc.org/MANUAL.html#creating-jupyter-notebooks-with-pandoc) and to .pdf conversion but Pandoctools surely capable of conversion to .html, .md.md or any [Pandoc output format](https://pandoc.org/MANUAL.html#general-options).**

Extras:

* If you need to capture Matplotlib plots please see [matplotlibhelper](https://github.com/kiwi0fruit/matplotlibhelper) (the approach showed in examples there can be used with other plot libraries).
* If you need to autonumber sections see [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) or [this SE question](https://stackoverflow.com/questions/48434961/how-to-customise-section-headings-to-start-with-letters-in-r-markdown)
* If you need criticmarkup support please consider using git repository with [git-time-machine](https://atom.io/packages/git-time-machine) for tracking changes, `<!-- html comments -->` for adding notes, [pigments](https://atom.io/packages/pigments) for highlighting text.


# Install

**If you have an antivirus then the first or two runs may fail - there may be errors like "Permission denied" because of the antivirus checking all the components.**


### Short instructions:

* **Either** (1.1) install 64-bit [Miniconda3](https://conda.io/miniconda.html) and:  
  (*on Unix:*)
  ```bash
  conda install -c defaults -c conda-forge pandoctools
  ```
  (*on Windows:*)
  ```batch
  conda install -c defaults -c conda-forge pandoctools git-bash
  ```
  (or install 64-bit [Git Bash](https://git-scm.com/downloads) instead of the conda package)
* **Or** (1.2) install 64-bit Python and:
  ```bash
  pip install pandoctools
  ```
  (if on Windows install 64-bit [Git Bash](https://git-scm.com/downloads))
* **Then** (2):
  ```bash
  pandoctools-ready
  ```
* But it's recommended to create a dedicated environment for the Pandoctools. See below.


### Via conda

* Create "pandoctools" conda environment (do not set custom prefix unless you want to set `root_env` in the [config](https://github.com/kiwi0fruit/pandoctools/tree/master/pandoctools/cli#defaultsini)):  
  (*on Unix*):
  ```bash
  cd $root_miniconda_prefix
  source ./bin/activate base
  conda config --add channels conda-forge
  conda config --add channels defaults
  conda update conda

  conda create -n pandoctools pandoctools
  source activate pandoctools
  pandoctools-ready
  ```
  (*on Windows*):
  ```bat
  cd /d %root_miniconda_prefix%
  call .\Scripts\activate base
  conda config --add channels conda-forge
  conda config --add channels defaults
  conda update conda

  conda create -n pandoctools pandoctools git-bash
  call activate pandoctools
  pandoctools-ready
  ```
  (or install 64-bit [Git Bash](https://git-scm.com/downloads) instead of the conda package; local Bash in the environment has priority)
* Just in case: the right way to remove conda environment 'myenv' is to run:
  ```bash
  conda remove -n myenv --all
  conda env remove -n myenv
  ```
  (in this particular order)


### Via pip

* Create pandoctools venv environment:  
  (*on Unix*):
  ```bash
  cd $root_python_prefix
  ./bin/python -m venv ./envs/pandoctools
  source ./envs/pandoctools/bin/activate

  pip install pandoctools
  pandoctools-ready
  ```
  (*on Windows*):
  ```bat
  cd /d %root_python_prefix%
  .\python -m venv .\envs\pandoctools
  call .\envs\pandoctools\Scripts\activate

  pip install pandoctools
  pandoctools-ready
  ```
  (then install 64-bit [Git Bash](https://git-scm.com/downloads))
* In contrast with conda installation Jupyter notebooks in pip do not support [activated python kernels](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/tips.md#install-python-kernel) (there is a strange bug).


# Useful tips (reload imported modules in Hydrogen, Python kernel, R kernel, Typescript kernel)

[Useful tips](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/tips.md)


# Alternatives to R Markdown (Markdown-based Literate Programming)

[Alternatives to R Markdown](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/alternatives_to_r_markdown.md)
