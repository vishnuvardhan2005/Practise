import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

movie_db = client['movie-db']

movies = movie_db['movies']

movies.insert_one({
    "name":"RRR",
    "rating":9,
})
movies.insert_many([
    {"name":"Liger","rating":1},
    {"name":"Beemala","rating":8},
])

print(movies.find_one())

print(movies.find_one({"name":"Liger"}))

print(movies.find({}))