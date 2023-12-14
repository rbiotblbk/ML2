import os 
from pathlib import Path 
from cleaner import CleanerCSV


os.chdir(Path(__file__).parent)





FILE_PATH = "./my_data.csv"
FILE_PATH1 = "./my_data_ffm.csv"
FILE_PATH2 = "./my_data_berlin.csv"
FILE_PATH3 = "./my_data_aachen.csv"



# Create instance

my_cleaned_file = CleanerCSV(FILE_PATH, with_load=True)
my_cleaned_file1 = CleanerCSV(FILE_PATH1, with_load=True)
my_cleaned_file2 = CleanerCSV(FILE_PATH2, with_load=True)
my_cleaned_file3 = CleanerCSV(FILE_PATH3, with_load=True)

 


print(my_cleaned_file.df.shape)