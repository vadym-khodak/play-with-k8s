import os
import platform
import time
import uuid

import redis
from flask import Flask, session

app = Flask(__name__)
app.config.update(SECRET_KEY=os.getenv("FLASK_SECRET_KEY", "some strong secret key"))
cache = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=os.getenv("REDIS_PORT", 6379))


@app.route("/ready")
def ready():
    try:
        return str(cache.ping()), 200
    except redis.exceptions.ConnectionError:
        return "Redis is not ready", 400


@app.route("/")
def index():
    session["uid"] = session.get("uid") or uuid.uuid4().hex

    retries = 3
    while True:
        try:
            counter = cache.incr(session["uid"])
            break
        except redis.exceptions.ConnectionError as err:
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(0.1)
    return f"""<div>
                 <h4>You visited this site {counter} times</h4>
                 <h5>Hostname: <strong>{platform.node()}</strong></h5>
               </div>"""


if __name__ == "__main__":
    app.run(host=os.getenv("FLASK_HOST", "0.0.0.0"), port=os.getenv("FLASK_PORT", 5000), debug=True)
