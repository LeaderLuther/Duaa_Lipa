import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.sql import text

#This is for connecting to our MySQL database
db_connection="mysql+pymysql://root:duaa_lipa@localhost/onekiss"

engine = create_engine(db_connection)

df = pd.read_csv("main.csv")

df.to_sql(name='user_table', con=engine, if_exists='append', index=False)