import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yml",
    "params.yml",
    "app.py",
    "main.py",
    "setup.py",
    "requirements.txt",
    "Dockerfile",
    "research/trials.ipynb",
]


for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Created directory: {fileDir}")
    
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)!=0) :
        with open(filePath, "w") as file:
            pass
        logging.info(f"Created file: {filePath}")
    else:
        logging.info(f"File {filePath} already exists and is not empty.")