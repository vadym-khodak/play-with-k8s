import os
import platform
import time

import redis
from flask import Flask, session, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config.update(SECRET_KEY=os.environ.get("FLASK_SECRET_KEY", "some strong secret key"))
app.config['CORS_HEADERS'] = 'Content-Type'
cache = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=os.environ.get("REDIS_PORT", 6379))


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
            time.sleep(0.1)
    return {"counter": counter, "hostName": platform.node(), "userId": session["uid"]}


if __name__ == "__main__":
    app.run(host=os.environ.get("FLASK_HOST", "localhost"), debug=True, port=os.environ.get("FLASK_PORT", 5000))
