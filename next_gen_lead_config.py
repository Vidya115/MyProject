import json
import psycopg2
from flask import Flask
from flask import request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
# Disable session pooling from sqlalchemy side use only postgres pool
from flask import jsonify
import os
from datetime import date
import logging as log
log.basicConfig()

app = Flask(__name__)
api = Api(app)
Base = declarative_base()
DATABASE_URL = "postgresql://postgres:vidya@localhost:5432/postgres"
USERNAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("USER_PASSWORD")
engine = create_engine(DATABASE_URL, echo=True, poolclass=NullPool)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()


