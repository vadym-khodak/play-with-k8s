import platform
import time
from typing import Optional

import redis
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
import config


def create_app():
    app = FastAPI()
    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    cache = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)

    @app.get("/ready")
    async def ready():
        try:
            return str(cache.ping()), 200
        except redis.exceptions.ConnectionError:
            return "Redis is not ready", 400

    @app.get("/")
    async def index(user: Optional[str] = Header(None)):

        retries = 3
        while True:
            try:
                counter = cache.incr(user)
                break
            except redis.exceptions.ConnectionError as err:
                if retries == 0:
                    raise err
                retries -= 1
                time.sleep(config.REDIS_SLEEP_TIME)

        return {"counter": counter, "hostName": platform.node(), "userId": user}

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
