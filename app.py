import os
import platform
import time

import redis
from flask import Flask, session, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config.update(SECRET_KEY=os.getenv("FLASK_SECRET_KEY", "some strong secret key"))
app.config['CORS_HEADERS'] = 'Content-Type'
cache = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=int(os.getenv("REDIS_PORT", 6379)))



@app.route("/ready")
def ready():
    try:
        return str(cache.ping()), 200
    except redis.exceptions.ConnectionError:
        return "Redis is not ready", 400


@app.route("/")
@cross_origin()
def index():
    session["uid"] = request.headers.get("user")

    retries = 3
    while True:
        try:
            counter = cache.incr(session["uid"])
            break
        except redis.exceptions.ConnectionError as err:
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(float(os.getenv("REDIS_SLEEP_TIME", 0.1)))

    return {"counter": counter, "hostName": platform.node(), "userId": session["uid"]}


if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST", "0.0.0.0"), port=int(os.getenv("FLASK_PORT", 5000)), debug=True
    )
