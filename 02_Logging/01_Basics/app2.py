

import logging 
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)




logging.basicConfig(filename= "./app.log", level = logging.DEBUG , 
                    format= '%(name)s - %(levelname)s - %(asctime)s - %(message)s')

 

logging.debug("This is my message")
logging.info("This is my message")
logging.warning("This is my message")
logging.error("This is my message")
logging.critical("This is my message")
logging.exception("This is my message")