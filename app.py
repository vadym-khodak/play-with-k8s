import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)


@app.route("/")
def index():
    retries = 5
    while True:
        try:
            counter = cache.incr("visits")
            break
        except redis.exceptions.ConnectionError as err:
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(0.5)
    return f"You visited this site {counter} times"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
