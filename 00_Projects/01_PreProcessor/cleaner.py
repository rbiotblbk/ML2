import pandas as pd 


class CleanerCSV():
    
    def __init__(self, file_path, with_load = False) -> None:
        self.orignial_file_path = file_path
        

        self.df_orignal =  pd.DataFrame()
        self.df =  pd.DataFrame()

        if with_load:
            self.load_data()

    
    def load_data(self):
        self.df_orignal = pd.read_csv(self.orignial_file_path) 
        
        
        self.df = self.df_orignal.copy() 


    def process_me(self):
        self.drop_na()

    def make_profile(self):
        print

    def drop_na(self):
        pass 


    def drop_duplicate(self):
        pass 


    def create_profile(self):
        pass 
        
         

        