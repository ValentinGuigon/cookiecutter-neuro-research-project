# Requirements

* [Python 3](https://www.python.org/downloads/)

## Install cookiecutter
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

## Important: if you choose to include R in your project from the cookiecutter script:
**In hooks/post_gen_project.py, make sure you change line 36 to suit your situation**:
* On Mac/Linux, the Rscript path is typically /usr/local/bin/Rscript or /usr/bin/Rscript.
* On Windows, the path for R version X.Y.Z is typically C:/Program Files/R/R-X.Y.Z/bin/Rscript.exe

## Important: if you choose to include MATLAB in your project from the cookiecutter script:
* The block that uses octave requires octave GNU installed, on path and working
* The block that uses matlab engine requires to call the appropriate python version by first setting up an install
* If no solution work, execute `init/init.m` by hand

# Project Structure
This structure is adapted from the TIER protocol 4.0 (https://www.projecttier.org/tier-protocol/protocol-4-0/root/). Each folder and subfolder has to have a descriptive and meaningful name, contains the files that are supposed to be in there, and a readme file documents the content of each.

```
    ┌── LICENSE
    ├── README.md          <- Top-level README for people using this project.
    ( if author file )
    ├── AUTHORS.md         <- Author information.
    |
    ├── .gitattributes     <- Set-up the directory.
    ├── .gitignore         <- Set-up the directory and tells Git which files to ignore.
    ├── .gitkeep           <- Set-up the directory and tells Git to keep the folder when empty.
    |
    ( if project includes matlab )
    ├── {{dir_name}}.prj  <- MATLAB project.
    |
    ( if project includes R )
    ├── {{dir_name}}.Rprj <- R project.
    ├── .Rhistory          <- R history.
    ├── .Rprofile          <- R profile.
    ├── renv.lock          <- Lock for R renv.
    |
    ├── data/
    │   ├── raw            <- Data files initially obtained or constructed at the beginning of the project.
    |   ├── intermediate   <- Data created at some point in the processing of the data that need to be saved temporarily.
    │   ├── processed      <- Data cleaned and processed.
    │   ├── stimuli        <- Data on experiment stimuli.
    │   └── README.md      <- Information on data sources and retrieval. 
    |
    ├── documents/
    │   ├── reports        <- Reports on analyses, such as html output from notebooks.
    │   └── README.md      <- Information on reports. 
    |
    ( if project includes matlab )
    ├── matlab_toolboxes/  <- A place for 3rd party MATLAB toolboxes.
    │   ├── toolbox/
    │   └── get_toolbox.sh <- Script to download toolboxes.
    |   └── README.md      <- Information on toolboxes. 
    |
    ├── output/            <- Saved figures, tables and other outputs generated during analysis.
    ( if project includes R )
    │   ├── R_environments <- Contains R environments, output by .R files and input of .Rmd files.
    │   ├── figures        <- Contains figures presented in the Journal Article.
    │   ├── supplementary  <- Contains figures presented in the Supplementary Materials.
    │   └── README.md      <- Information on data outputs and about scripts that produce them. 
    |
    ├── playground/        <- Playground prior to Abstraction and Refactoring data manipulation into Scripts
    │   ├── data
    │   ├── notebooks
    │   ├── outputs
    │   ├── scripts
    │   └── README.md
    |
    ( if project includes R )
    ├── renv/              <- R renv to restore a snapshot of R environment containing installed packages with versioning. Executed by R `renv::activate()`
    │   ├── activate.R
    │   ├── settings.json
    │   └── README.md      <- Information on the snapshot of libraries. 
    |
    ( if project includes matlab )
    ├── resources/project/ <- Contains the MATLAB project
    │   └── ...      
    │
    ├── scripts/           <- Jupyter notebooks, MATLAB code and anything else that constitutes analysis.
    │   ├── extraction     <- Preprocessing scripts that extract data from raw files for processing.
    │   ├── processing     <- Scripts that transform extracted data files into processed data files.
    │   ├── analysis       <- Scripts that produce the results, such as figures, tables and statistics.
    │   ├── reporting      <- Scripts that produce the reports on the results.
    │   ├── src            <- Source scripts used across scripts, such as models, utilities, packages.
    │   ├── supplementary  <- Scripts that produce the results present in the Supplementary Materials.
    │   └── README.md      <- Any information about the analysis, such as execution order. 
    │
    ├── stimuli/           <- Contains the stimuli
    │   └── ...      
    |
    ├── init/           <- Contains the init scripts
    |
    ( if project includes python )
    │   ├── __init__.py    <- Initiate a python package.
    │   └── module.py      <- A Python module.
    |
    ( if project includes matlab )
    │   └── init.m         <- Initiate a MATLAB environment.
    |
    ( if project includes R )
        └──  init.R         <- Initiate a R environment.
    
```
