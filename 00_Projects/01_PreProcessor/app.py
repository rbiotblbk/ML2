import os 
from pathlib import Path 
from cleaner import CleanerCSV


os.chdir(Path(__file__).parent)





FILE_PATH = "./my_data.csv"
 



# Create instance

my_cleaned_file = CleanerCSV(FILE_PATH, with_load=True)
my_cleaned_file.process_me()

# In Streamlit
my_cleaned_file.df


 