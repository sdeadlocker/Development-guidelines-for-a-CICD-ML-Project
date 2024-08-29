import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# Define a list of folders and files
paths = [
    ".jenkins/Jenkinsfile",                       # Jenkins pipeline definition
    "config/dev.env",                             # Dev environment config
    "data/raw/",                                  # data directory
    "data/processed/",                            
    "model/",                                     # directory for model artifacts
    "src/components/__init__.py",                
    "src/components/data_ingestion.py",           
    "src/components/data_preprocessing.py",       
    "src/components/feature_engineering.py",      
    "src/pipeline/__init__.py",                  
    "src/pipeline/train_model.py",                
    "src/pipeline/inference.py",                  
    "src/utils/__init__.py",                     
    "src/utils/helper_functions.py",              # Utility functions
    "tests/__init__.py",                          
    "requirements.txt",                           
    "README.md",                                  
    "research/test.ipynb",                        # file for running experiments
    "Dockerfile",                                 
    ".gitignore"                                  
]

# create directories and empty files
def create_paths(path_list):
    for path in path_list:
        if path.endswith("/"):
            # It's a directory
            Path(path).mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {path}")
        else:
            # Ensure the directory for the file exists
            dir_name = Path(path).parent
            if dir_name:  # Ensure directory name is not empty
                dir_name.mkdir(parents=True, exist_ok=True)
            # Create an empty file
            Path(path).touch()
            logging.info(f"Created file: {path}")

if __name__ == "__main__":
    create_paths(paths)
    logging.info("Folder and file structure created successfully.")
