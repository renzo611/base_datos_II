from database.redis_db import redis_client
from database.mongo_db import mongo_client

collection_name = mongo_client["lotes"]

item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}


try:
    collection_name.insert_one(item_1)
    print("✅ Documento insertado en MongoDB correctamente")
except Exception as e:
    print(f"Error conectando a Redis: {e}")