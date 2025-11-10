"""
Redis connection module
"""
import redis.asyncio as redis
from app.config.config import settings
from app.log.logger import get_database_logger

logger = get_database_logger()

redis_client = None

async def get_redis_client():
    """
    Get redis client
    """
    return redis_client

async def connect_to_redis():
    """
    Connect to redis
    """
    global redis_client
    try:
        redis_client = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
        await redis_client.ping()
        logger.info("Connected to Redis: %s", settings.REDIS_URL)
    except Exception as e:
        logger.error(f"Failed to connect to Redis: {str(e)}")
        raise

async def disconnect_from_redis():
    """
    Disconnect from redis
    """
    if redis_client:
        try:
            await redis_client.close()
            logger.info("Disconnected from Redis")
        except Exception as e:
            logger.error(f"Failed to disconnect from Redis: {str(e)}")