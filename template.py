import os
from pathlib import Path
import logging

# Logging info
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Data-science-project'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # Folder src/proejct name with __init__
    f"src/{project_name}/components/__init__.py", # Components folder with __init__
    f"src/{project_name}/utils/__init__.py", # utils folder with __init__
    f"src/{project_name}/utils/common.py", # common.py file within utils
    f"src/{project_name}/config/__init__.py", # Config folder with __init__
    f"src/{project_name}/config/configuration.py", # configuration.py file within config folder
    f"src/{project_name}/pipeline/__init__.py", # pipeline folder
    f"src/{project_name}/entity/__init_.py", # entity folder
    f"src/{project_name}/entity/config_entity.py", # Config_entity file within entity folder
    f"src/{project_name}/constants/__init__.py", # Constants folder
    "config/config.yaml",
    "params.yaml", # Machine Learning params
    "schema.yaml",
    "main.py",
    "Dockerfile", # Dockerization
    "setup.py", # Setup for pypy packaging
    "research/research.ipynb", # Notebook to explore and research
    "templates/index.html", # Flask integration with html
    # "requirement.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # os.path.split returns head and tail of filepath

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # File directory/folder creation if doesn't exists
        logging.info(f"Creating directory {filedir}.")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')
    else:
        logging.info(f"{filename} is already exists.")