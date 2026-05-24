from pymongo import MongoClient

collection_name = "products_121225_ptm_Baranovskyi"

class MongoDB:
    def __init__(self):
        self.__client = MongoClient(
            "mongodb://ich_editor:verystrongpassword"
            "@mongo.itcareerhub.de/?readPreference=primary"
            "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
        )
        self.__db = self.__client["ich_edit"][collection_name]

        self.__client.admin.command("ping")
        print("Connection successful!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.close()
        print("Connection closed")
        return False

    def clear(self):
        self.__db.delete_many({})
        return "Collection cleared"

    def insert_products(self, products):
        result = self.__db.insert_many(products)
        return f"{len(result.inserted_ids)} products inserted."

    def update_prices(self, multiplier):
        result = self.__db.update_many(
            {},
            [{"$set": {"price": {"$multiply": ["$price", multiplier]}}}]
        )
        return f"Prices updated for {result.modified_count} products."

    def get_all(self):
        return list(self.__db.find({}, {"_id": 0}))


products = [
    {"name": "1",   "price": 111, "stock": 11},
    {"name": "2",    "price": 222,  "stock": 22},
    {"name": "3", "price": 333,  "stock": 33},
]

with MongoDB() as mongo:
    print(mongo.clear())
    print(mongo.insert_products(products))
    # print(mongo.update_prices(1.20))
    print("\nUpdated products:")

    for product in mongo.get_all():
        print(f"- {product['name']} - ${product['price']:.2f}")