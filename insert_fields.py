from bson import ObjectId
from database.mongo_db import mongo_client
from database.redis_db import redis_client
from datetime import datetime
import json

# ---------------------
# MongoDB - Insertar horno y lote
# ---------------------

# Insertar horno
oven = {
    "_id": ObjectId("67f3f1d0f93c97b2aec11525"),
    "name": "Horno 2",
    "location": "Chilecito"
}
mongo_client.ovens.insert_one(oven)
print(f"[MongoDB] Insertado horno: {oven}")

# Insertar lote
nut_batch = {
    "_id": ObjectId("67f51e064126a6e6cba17bc1"),
    "nut_type": "HALF",
    "start_date": datetime(2025, 4, 8, 10, 0, 53, 789000),
    "end_date": None,
    "initial_weight": 50.36,
    "initial_humidity": 36.25,
    "target_humidity": 20.23,
    "oven_id": "67f3f1d0f93c97b2aec11525",
    "drying_history": [],
    "status": "IN_PROGRESS"
}
mongo_client.nut_batches.insert_one(nut_batch)
print(f"[MongoDB] Insertado lote: {nut_batch}")

# ---------------------
# Redis - Insertar datos temporales del lote
# ---------------------

batch_id = "67f51e064126a6e6cba17bc1"
redis_key = f"batch:{batch_id}:data"

# Datos temporales
real_time_data = [
    {"temperature": 55, "humidity": 31, "weight": 13, "gas_consumption": 12, "timestamp": "2025-04-08T23:20:04.904431"},
    {"temperature": 53, "humidity": 30, "weight": 12, "gas_consumption": 15, "timestamp": "2025-04-08T23:20:29.736722"},
    {"temperature": 12, "humidity": 17, "weight": 10, "gas_consumption": 18, "timestamp": "2025-04-08T23:27:17.408712"},
    {"temperature": 12, "humidity": 17, "weight": 10, "gas_consumption": 18, "timestamp": "2025-04-08T23:27:45.257424"},
    {"temperature": 12, "humidity": 17, "weight": 10, "gas_consumption": 18, "timestamp": "2025-04-09T00:06:34.867247"},
    {"temperature": 12, "humidity": 17, "weight": 10, "gas_consumption": 18, "timestamp": "2025-04-09T00:08:16.035295"},
]

for i, entry in enumerate(real_time_data, start=1):
    entry["batch_id"] = batch_id
    redis_client.rpush(redis_key, json.dumps(entry))
    print(f"[Redis] Insertado registro #{i} en {redis_key}")

print("\n✅ Todos los datos fueron insertados correctamente en MongoDB y Redis.")
