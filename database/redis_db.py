import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None

def get_redis_connection():
    """Función para obtener una conexión a Redis."""
    return redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True  # Para devolver strings en lugar de bytes
    )

redis_client = get_redis_connection()
