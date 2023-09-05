from glob import glob
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.append("/init")

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


# No-init actions
if not '{{cookiecutter.include_python}}' == 'yes':
    remove('init/__init__.py')

if not '{{cookiecutter.include_matlab}}' == 'yes':
    remove('matlab_toolboxes')
    remove('init/init.m')

if not '{{cookiecutter.include_r}}' == 'yes':
    remove('output/R_environments')
    remove('init/init.R')

if not '{{cookiecutter.include_python}}' == 'yes' and not '{{cookiecutter.include_matlab}}' == 'yes' and not '{{cookiecutter.include_r}}' == 'yes':
    remove('init/')



# Remove un-used files
if not '{{cookiecutter.create_author_file}}' == 'yes':
    remove('AUTHORS.md')
    
if '{{ cookiecutter.open_source_license }}' == 'Not open source':
    remove('LICENSE')



# Init
if '{{cookiecutter.include_r}}' == 'yes':
    command = 'C:/Program Files/R/R-4.3.1/bin/x64/Rscript'
    arg = '--vanilla' 
    subprocess.call([command, arg, "init/init.R"], shell=True)

if '{{cookiecutter.include_python}}' == 'yes':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    subprocess.run(["python", "init/init.py"])
    os.system(f'pip freeze > "{"requirements.txt"}"')

''' uses octave
if '{{cookiecutter.include_matlab}}' == 'yes':
    from oct2py import Oct2Py
    path = Path('.')
    octave.addpath(octave.genpath('path/init')) 
    octave.savepath() 
    octave.run('init.m')
'''
''' uses matlab engine, 
see https://fr.mathworks.com/matlabcentral/answers/553642-how-do-i-chose-the-correct-version-of-python-when-trying-to-install-the-matlab-engine-api
if '{{cookiecutter.include_matlab}}' == 'yes':
    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.addpath(init)
    eng.init(nargout=0)
'''



# Make the shell scripts executable
for sh_script in glob("*.sh"):
    os.chmod(sh_script, 0o744)



# Remove init folder at the end of the post_gen
remove('init/')