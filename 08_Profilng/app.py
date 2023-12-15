# pip install ydata-profiling

import os 
import pandas as pd 
from pathlib import Path 


from ydata_profiling import ProfileReport

os.chdir(Path(__file__).parent) 



INPUT_FILE = "./my_data.csv" 
OUTPUT_FILE = "./profile.html"


# 1. Load Data 
df = pd.read_csv(INPUT_FILE)


# 2. Create the profile
profile = ProfileReport(df)


# 3. Save the output profile
profile.to_file(output_file = OUTPUT_FILE )