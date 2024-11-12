import os
from pathlib import Path
import logging


project_name = "Digit_Recognizer"

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

list_of_files = [
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    "setup.py",
    ".gitignore",
    "requirements.txt",
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configration.py',
    "research/trials.ipynb",
    "templates/index.html"
    
]


for file_path in list_of_files:
    file_path = Path(file_path)

    file_dir , file = os.path.split(file_path)
    
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory; {file_dir} for the file: {file}")

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file_path, "w") as f:
            f.write(f"# {file}")
            logging.info(f"Created file: {file}")

    else:
        logging.info(f"File: {file} already exists.")

