from pymongo import MongoClient



def add_restaurant(mongo_host, data):
    """
    Add data
    :param mongo_host:
    :param data:
    :return:
    """
    client = MongoClient(mongo_host)
    db = client['test']
    inserted_id = db.my_restaurants.insert_one(data).inserted_id
    client.close()
    print ("ID del restaurante creado ={}".format(inserted_id))
    return inserted_id


def update_restaurant(mongo_host, id, data):
    """
    Update restaurant
    :param mongo_host:
    :param id:
    :param data:
    :return:
    """
    client = MongoClient(mongo_host)
    db = client['test']
    db.my_restaurants.update_one({'_id': id}, {"$set": data})
    client.close()

def get_restaurant(mongo_host, id):
    """
    Get a restaurant by id
    :param mongo_host:
    :param id:
    :return:
    """
    client = MongoClient(mongo_host)
    db = client['test']
    client.close()
    result = db.my_restaurants.find({'_id': id})
    return result[0]


def get_restaurant_with_query(mongo_host, query):
    """
    Executes the query
    :param mongo_host:
    :param query:
    :return:
    """
    client = MongoClient(mongo_host)
    db = client['test']
    client.close()
    results = db.my_restaurants.find(query)
    return results

