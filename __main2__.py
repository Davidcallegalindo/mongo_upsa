from pymongo import MongoClient
import json
from bson import Code

MONGO_HOST = "127.0.0.1:27017"
FILE_MOCK = "MOCK_DATA.json"
DATA = [
    {
        "first_name": "Manuel",
        "last_name": "Gomez",
        "email": "manogo@gmail.com",
        "gender": "Male",
        "ip_address": "15.208.64.26",
        "Latitude": 43.6342238,
        "Altitude": -3.41144,
        "City": "Madrid",
        "University": "Upsa"
    },
    {
        "first_name": "Lucia",
        "last_name": "Sanchez",
        "email": "lucisan@gmail.com",
        "gender": "Female",
        "ip_address": "5.208.64.76",
        "Latitude": 43.1342238,
        "Altitude": -2.41144,
        "City": "Salamanca",
        "University": "UPSA"
    },
    {
        "first_name": "Sergio",
        "last_name": "Suarez",
        "email": "sergiosua@gmail.com",
        "gender": "Male",
        "ip_address": "5.208.65.29",
        "Latitude": 43.1342238,
        "Altitude": -2.61144,
        "City": "Salamanca",
        "University": "UPSA"
    }
]


def get_print_from_cursor(message, cursor):
    print(message)
    for item in cursor:
        print(item)


def import_json(database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    with open(FILE_MOCK) as f:
        file_data = json.load(f)
        db.get_collection(collection).insert_many(file_data)
    client.close()


def insert_data(data, database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    db.get_collection(collection).insert_many(data)
    client.close()

def run_query(database, collection, query):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    client.close()
    result = db.get_collection(collection).find(query)
    return result


def clean_collection(database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    client.close()
    db.get_collection(collection).delete_many({})


def run_count(database, collection, query):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    client.close()
    result = db.get_collection(collection).count_documents(query)
    return result


def calcula_male_female():
    """
    APARTADO 3
    :return:
    """
    query_one = {'gender': 'Male'}
    query_two = {'gender': 'Female'}
    count_male = run_count(my_database, my_collection, query_one)
    count_female = run_count(my_database, my_collection, query_two)
    male_result = (count_male) * 100 / (count_male + count_female)
    female_result = (count_female) * 100 / (count_male + count_female)
    print(f"Male result {male_result}")
    print(f"Female result {female_result}")


def update_ip_user_and_check(database, collection, new_ip, name):
    """
    APARTADO 4
    :param new_ip:
    :param old_ip:
    :return:
    """

    client = MongoClient(MONGO_HOST)
    db = client[database]
    data = {'ip_address': new_ip}
    query = {'first_name': name}
    db.get_collection(collection).update_one(query, {"$set": data})
    client.close()
    result = run_query(database, collection, query)

    print('UPDATED¿?:' + str(result[0]['ip_address'] == new_ip))


def query_latitude_altitude(database, collection):
    query = {"$and": [{"Latitude": {"$gte": 30.00}}, {"Altitude": {"$lt": 10.000}}]}
    result = run_query(database, collection, query)
    get_print_from_cursor(f'Query latitud altitud***\n', result)




def using_map_reduce(database, collection):
    """DEMO MAP REDUCE"""
    map = Code("function () {"
               "    emit(this.gender, 1);"
               "}")
    reduce = Code("function (key, values) {"
                  "  var total = 0;"
                  "  for (var i = 0; i < values.length; i++) {"
                  "    total += values[i];"
                  "  }"
                  "  return total;"
                  "}")

    client = MongoClient(MONGO_HOST)
    db = client[database]
    result = db.get_collection(collection).map_reduce(map, reduce, "myresults")
    get_print_from_cursor('Map reduce', result.find())











my_database = "masterDb"
my_collection = "users"
# APARTADO 1
import_json(my_database, my_collection)

## APARTADO 2
insert_data(DATA, my_database, my_collection)

# APARTADO 3
calcula_male_female()

# APARTADO 4
update_ip_user_and_check(my_database, my_collection, '﻿109.150.230.156/24', 'Jervis')



# APARTADO 5

query_latitude_altitude(my_database, my_collection)
## BONUS TRACK

using_map_reduce(my_database, my_collection)
# clean_collection(my_database, my_collection)
