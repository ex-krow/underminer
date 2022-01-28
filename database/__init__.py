from decouple import config
from neo4j import GraphDatabase

db_url = config("DATABASE_URL")
db_username = config("DATABASE_USERNAME")
db_pass = config("DATABASE_PASSWORD")
