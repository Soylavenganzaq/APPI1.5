import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from sqlalchemy import Column, Integer, String
from models.db import Base



class user (base):
    __tablename__ ="users"
    id= column(Integer, primary_key=True, index=True)
    username = column(string(50), unique=True, nullable=False)
    password = column(string(255),nullable=False)
