from fastapi import FastAPI
import psycopg2
from urllib.parse import urlparse
import os

app = FastAPI()

# Get the database url from the environment variable
DATABASE_URL = os.environ['DATABASE_URL']

# Parse the url to get the necessary information
result = urlparse(DATABASE_URL)
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port

# Connect to the database
connection = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname,
    port = port
)

@app.get("/")
async def root():
    return {"message": "Hello World"}