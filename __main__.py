import mongo_utils


def get_print_from_cursor(message, cursor):
    print (message)
    for item in cursor:
        print (item)


DATA_TEST = {
    "name" : "Casa Paco",
    "Country": "Spain",
    "Telephone_number": "600600600",
    "score": 96

}

DATA_TEST_2 = {
    "name" : "Peter's House",
    "Country": "UK",
    "Telephone_number": "44600600600",
    "score": 65
}

DATA_TEST_3 = {
    "name" : "NZ Pub",
    "Country": "NZ",
    "Telephone_number": "77600600600",
    "score": 38
}


MONGO_HOST = "127.0.0.1:37017"

id_rest = mongo_utils.add_restaurant(MONGO_HOST, DATA_TEST)

mongo_utils.update_restaurant(MONGO_HOST, id_rest, {"Country": "France"})

data_from_db = mongo_utils.get_restaurant(MONGO_HOST, id_rest)
mongo_utils.add_restaurant(MONGO_HOST, DATA_TEST_2)
mongo_utils.add_restaurant(MONGO_HOST, DATA_TEST_3)

query = {"$or": [{"score": {"$gt": 50}}, {"score": {"$lt": 100}}]}
results = mongo_utils.get_restaurant_with_query(MONGO_HOST, query)
get_print_from_cursor("Or query:", results)

query = {"$and": [{"score": {"$gt": 50}}, {"score": {"$lt": 100}}]}
results = mongo_utils.get_restaurant_with_query(MONGO_HOST, query)

get_print_from_cursor("And query", results)

