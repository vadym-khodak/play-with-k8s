import os


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_SLEEP_TIME = int(os.getenv("REDIS_SLEEP_TIME", 0.1))
