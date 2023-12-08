import logging
from logging.config import fileConfig 


import os
from pathlib import Path 
os.chdir(Path(__file__).parent)

# Read the config file for logger and configer your logger automatically
fileConfig("logging.ini")

logger = logging.getLogger() # root 



logger.info(f"Hello Mohamed")