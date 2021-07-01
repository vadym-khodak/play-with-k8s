import os
import platform
import time
import uuid

import redis
from flask import Flask, session

app = Flask(__name__)
app.config.update(SECRET_KEY=os.environ.get("FLASK_SECRET_KEY", "some strong secret key"))
cache = redis.Redis(host="redis", port=6379)


@app.route("/")
def index():
    session["uid"] = session.get("uid") or uuid.uuid4().hex

    retries = 5
    while True:
        try:
            counter = cache.incr(session["uid"])
            break
        except redis.exceptions.ConnectionError as err:
            if retries == 0:
                raise err
            retries -= 1
            time.sleep(0.5)
    return f"""<div>
                 <h4>You visited this site {counter} times</h4>
                 <h5>Hostname: <strong>{platform.node()}</strong></h5>
               </div>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
