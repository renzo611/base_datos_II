import os
from dotenv import load_dotenv
import redis

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

print(f"REDIS_HOST: {REDIS_HOST}")
print(f"REDIS_PORT: {REDIS_PORT}")
print(f"REDIS_DB: {REDIS_DB}")
print(f"REDIS_PASSWORD: {REDIS_PASSWORD}")


def get_redis_connection():
    """Función para obtener una conexión a Redis."""
    return redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True
    )

redis_client = get_redis_connection()
print(redis_client)