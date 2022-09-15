import sys
# If you are not able to import constant py file use below code
sys.path.insert(1, 'etl_pandas\metadata')
from constant import connection


#from etl_pandas.metadata.constant import CITY_COL_DICT
import pandas as pd

def extract(type: str, source: str):
    # Read data from mysql database 
    if type=="db":
        output_df = pd.read_sql(f'SELECT * FROM {source}', con=connection())
    
    if type=="csv":
        # read data from filesystem
        output_df = pd.read_csv(source)
    
    return output_df


