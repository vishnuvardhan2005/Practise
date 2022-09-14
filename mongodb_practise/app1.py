from pprint import pprint
import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

movie_db = client['movie-db']

movies = movie_db['movies']

print(movies.find({}))