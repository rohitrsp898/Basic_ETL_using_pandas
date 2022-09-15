import pandas as pd
# extracting data from filesystem
# IMported required libraries and modules
import sys
# If you are not able to import constant py file use below code
sys.path.insert(1, 'etl_pandas\metadata')

from constant import connection, CITY_COL_DICT, COUNTRY_LANGUAGE_COL_DICT, COUNTRY_COL_DICT, \
    JOIN_TYPE,JOIN_ON_COLUMNS, SPEC_COLS

    
from extract import extract
from transform import rename_cols, join_df, specific_cols
from load import load



#### ----- Extract ----- ####

# Extracting CITY and COUNTRY data from MYSQL
city_df = extract("db","city")
country_df = extract("db","country")

# Extracting COUNTRYLANGUAGE data from FileSystem
country_language_df = extract("csv","etl_pandas\data\countrylanguage.csv")

print(city_df.dtypes)
print(country_df.dtypes)
print(country_language_df.dtypes)


#### ----- Transformation ----- ####

# 1. Rename Columns
city_df = rename_cols(city_df, CITY_COL_DICT)
country_df = rename_cols(country_df, COUNTRY_COL_DICT)
country_language_df = rename_cols(country_language_df, COUNTRY_LANGUAGE_COL_DICT)

# 2. Join DF with common column "country_code"
country_city_df=join_df(country_df, city_df, JOIN_ON_COLUMNS, JOIN_TYPE)
country_city_language_df= join_df(country_city_df, country_language_df, JOIN_ON_COLUMNS, JOIN_TYPE)

# 3. Get specific cols
country_city_language_df = specific_cols(country_city_language_df, SPEC_COLS)



#### ----- Load Data ----- ####

# MySQL 
load("db",country_city_language_df, "countrycitylanguage")

# FileSystem
load("csv",country_city_language_df, "etl_pandas/output/countrycitylanguage.csv")



    
     


    
    
