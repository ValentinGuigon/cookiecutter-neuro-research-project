import os 
from pathlib import Path
import venv

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  
venv_dir = os.path.join(parent_dir, 'venv')

# Create the virtual environment
venv.create(venv_dir, with_pip=True)