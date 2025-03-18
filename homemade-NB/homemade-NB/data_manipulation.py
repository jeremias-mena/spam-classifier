import pandas as pd 

class DataFrameOperations:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def create_column_from_function(self, new_column_name:str, column_to_apply_function: str, function: function):
        self.df[new_column_name] = self.df[column_to_apply_function].apply(function)  
        return self.df
    



