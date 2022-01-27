from neo4j import GraphDatabase
from decouple import config

db_url = config("DATABASE_URL")
db_username = config("DATABASE_USERNAME")
db_pass = config("DATABASE_PASSWORD")

