import pandas as pd
import numpy as np

from sqlalchemy import create_engine
from sqlalchemy.sql import text

#This is for connecting to our MySQL database
db_connection = "mysql+pymysql://gfxgrhxf9maut1s0ryko:pscale_pw_HgKBqBiaGayJJfuGLVEUVPbZkXwoitRRr6RXiXcBF0Q@aws.connect.psdb.cloud/one_kiss_website?charset=utf8mb4"
#db_connection="mysql+pymysql://root:duaa_lipa@localhost/onekiss"
#connect_args={
#        "ssl": {
#            "ca": "/etc/ssl/certs/ca-certificates.crt",
#	        }
#	    }	

engine = create_engine(
	db_connection, 
  connect_args={
         "ssl": {
             "ca": "/etc/ssl/cert.pem",
          }
      } 
	)

df = pd.read_csv("main.csv")

df.to_sql(name='user_table', con=engine, if_exists='append', index=False)