By {{cookiecutter.full_name}}

{% set dir_name = cookiecutter.project_name.replace(' ', '').replace('-', '') -%}

{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name.replace('-', ' ').replace('_', ' ').title() }}
{{ cookiecutter.description }}

## Requirements

{%- if cookiecutter.include_python == 'yes' %}  

* Either Conda package manager (I recommend the lightweight version miniconda)
* Or pip package manager

{%- endif %}  

{%- if cookiecutter.include_matlab == 'yes' %}

* Matlab 2020b minimum

{%- endif %}  

{%- if cookiecutter.include_r == 'yes' %}  

* R 4.3.1
* R::renv
* JAGS 4.3.1
* Rtools 4.3
* R::rjags

{%- endif %}  

## Installing and removing the environment

{%- if cookiecutter.include_python == 'yes' %}

An environment is specified in requirements.txt and may be installed using the appropriate bash scripts.

To install:
```
pip install -r requirements.txt
```
To update the list of requirements:
```
pip freeze requirements.txt
```

A conda environment.yml may be more suitable if you want to install/remove jupyter kernels for the environment.
> In such a case, if these don't execute, you might need to change the file permissions with chmod u+x *.sh.

{%- endif %}


{%- if cookiecutter.include_matlab == 'yes' %}

A MATLAB project was created. Ressources are located in the folder with the same name. Open it with MATLAB.

{%- endif %}


{%- if cookiecutter.include_r == 'yes' %}

A R project was created. Open it with R.
An environment for R was created via renv. It is specified across `renv.lock`, `.Rprofile`, `renv/settings.json` and `renv/activate.R`. To operate with the project renv, first open the R Project `{{dir_name}}Rproj`.

To restore the environment:
```
renv::init()
renv::restore()
```

To deactivate the environment:
```
renv::deactivate()
```
This removes the renv auto-loader from the project .Rprofile, but doesn’t touch any other renv files used in the project. 

To later re-activate the environment:
```
renv::activate()
```

To completely remove the environment:
```
renv::deactivate(clean = TRUE)
```

{%- endif %}

## Project Structure
This structure is adapted from the TIER protocol 4.0 (https://www.projecttier.org/tier-protocol/protocol-4-0/root/). Each folder and subfolder has to have a descriptive and meaningful name, contains the files that are supposed to be in there, and a readme file documents the content of each. 

```
{{dir_name}}/
    ├── LICENSE
    ├── README.md          <- Top-level README for people using this project.
{%- if cookiecutter.create_author_file == 'yes' %}
    ├── AUTHORS.md         <- Author information.
{%- endif %}
    |
    ├── .gitattributes     <- Set-up the directory.
    ├── .gitignore         <- Set-up the directory and tells Git which files to ignore.
    ├── .gitkeep           <- Set-up the directory and tells Git to keep the folder when empty.
    |
{%- if cookiecutter.include_matlab == 'yes' %}
    ├── {{dir_name}}.prj  <- MATLAB project.
{%- endif %}
    |
{%- if cookiecutter.include_r == 'yes' %}
    ├── {{dir_name}}.Rprj <- R project.
    ├── .Rhistory          <- R history.
    ├── .Rprofile          <- R profile.
    ├── renv.lock          <- Lock for R renv.
{%- endif %}    
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
{%- if cookiecutter.include_matlab == 'yes' %}
    ├── matlab_toolboxes/  <- A place for 3rd party MATLAB toolboxes.
    │   ├── toolbox/
    │   └── get_toolbox.sh <- Script to download toolboxes.
    |   └── README.md      <- Information on toolboxes. 
{%- endif %}    
    |
    ├── output/            <- Saved figures, tables and other outputs generated during analysis.
{%- if cookiecutter.include_r == 'yes' %}
    │   ├── R_environments <- Contains R environments, output by .R files and input of .Rmd files.
{%- endif %}   
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
{%- if cookiecutter.include_r == 'yes' %}
    ├── renv/              <- R renv to restore a snapshot of R environment containing installed packages with versioning. Executed by R `renv::activate()`
    │   ├── activate.R
    │   ├── settings.json
    │   └── README.md      <- Information on the snapshot of libraries. 
{%- endif %}  
    |
{%- if cookiecutter.include_matlab == 'yes' %}
    ├── resources/project/ <- Contains the MATLAB project
    │   └── ...      
{%- endif %} 
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
{%- if cookiecutter.include_python == 'yes' %}
    │   ├── __init__.py    <- Initiate a python package.
    │   └── module.py      <- A Python module.
{%- endif %}
    |
{%- if cookiecutter.include_matlab == 'yes' %}
    │   └── init.m         <- Initiate a MATLAB environment.
{%- endif %}
    |
{%- if cookiecutter.include_r == 'yes' %}
    │   └──  init.R         <- Initiate a R environment.
{%- endif %}
    |
    
 ```

{% if is_open_source %}

Free software: {{ cookiecutter.open_source_license }} 

{% endif %}