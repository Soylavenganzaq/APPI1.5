from sqlalchemy import column, Integer, string
from db import base



class user ():
    __tablename__ ="users"
    id= column(Integer, primary_key=True, index=True)
    username = column(string(50), unique=True, nullable=False)
    password = column(string(255),nullable=False)
