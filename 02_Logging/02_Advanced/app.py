import os 
import logging 
from car import Car
from pathlib import Path 

os.chdir(Path(__file__).parent)


# Create Logger from Logging

logger = logging.getLogger() # root logger

 


logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')


# Creaete a file handler logger
file_handler = logging.FileHandler("app2.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)



# Create a stream handler (in terminal)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
# stream_handler.setFormatter(formatter)


# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)








logger.info("This is my message")

vw = Car()

vw.drive(100)

print(vw)
