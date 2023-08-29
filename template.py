import os
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]: %(message)s")

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for path in list_of_files:
    path = Path(path)
    dir, name = os.path.split(path)
    
    if (dir != ""):
        os.makedirs(dir, exist_ok = True)
        logging.info("Created directory: {dir} for file: {name}".format(dir = dir, name = name))
        
    if ((not os.path.exists(path)) or (os.path.getsize(path) == 0)):
        with open(path, "w") as f:
            f.write("")
            logging.info("Created empty file: {name}".format(name = name))
    else:
        logging.info("File already exists: {name}".format(name = name))