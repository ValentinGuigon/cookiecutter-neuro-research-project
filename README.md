## Requirements

* [Python 3](https://www.python.org/downloads/)
* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

You can install [Cookiecutter Python package](https://cookiecutter.readthedocs.io/en/latest/installation.html) easily with conda:
``` bash
conda install -c conda-forge cookiecutter
```

Or with pip:
``` bash
pip install --user cookiecutter
```

Note that conda may be recommended, especially if you wish to work with Jupyter notebooks and restore kernels.


## To start a new project
``` bash
cookiecutter gh:/ValentinGuigon/cookiecutter-neuro-research-project
```
(*this should be run from the location that you want the project folder to live, or you will need to move the directory around later*)

## To connect the new project to a GitHub repository

We now want to connect this local repository to a github repo. This can be done directly from the command line using the [Github Command Line Interface](https://github.com/cli/cli#installation). You will have to install it following one of the methods described [here](https://github.com/cli/cli#installation)

1. If using the Github Command Line Interface, simply navigate to the project root folder and type:
``` bash
git init -b main
```

2. Then, go to GitHub.com and create a new remote repository as Public or Private given your project.

3. Finally, type in the Command Line Interface the following, by specifying your username as well as the name of the new remote repository you just created on GitHub.com:
``` bash
git remote add origin git@github.com:<username>/<new_project>.git
```

## Important to use cookiecutter when R is part of the script:
**In hooks/post_gen_project.py, make sure you change line 36 to suit your situation**:
* On Mac/Linux, the Rscript path is typically /usr/local/bin/Rscript or /usr/bin/Rscript.
* On Windows, the path for R version X.Y.Z is typically C:/Program Files/R/R-X.Y.Z/bin/Rscript.exe

## Important to use cookiecutter when MATLAB is part of the script:
* The block that uses octave requires octave GNU installed, on path and working
* The block that uses matlab engine requires to call the appropriate python version by first setting up an install
* If no solution work, execute `init/init.m` by hand
