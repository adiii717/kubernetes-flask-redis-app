from flask import Flask
from flask import render_template
import os
from flask import Flask
from redis import Redis, RedisError
import socket
import os




app = Flask(__name__)


@app.route("/")

def sample_run_report():
    redis_conn = Redis(host=os.environ.get('REDIS_HOST', "redis-leader.default.svc.cluster.local"), port=6379, db=0)
    redis_conn.set("key", "foo")
    val = redis_conn.get("key")
    return val
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)