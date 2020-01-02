from redis import Redis  # pylint: disable=import-error
from jaspion import Jaspion


# Freeswitch data to connection
freeswitch = {"host": "127.0.0.1", "password": "ClueCon", "port": 8021}

# Redis data to connection
redis = {"host": "127.0.0.1", "port": 6379}

# Instance of Jaspion and Redis conn
app = Jaspion(**freeswitch)
conn = Redis(**redis)

# Save all register in redis with expires of sip message.
@app.handle("sofia::register")
def register(event):
    key = "registers:%s" % event["call-id"]
    ttl = int(event["expires"])
    conn.hmset(key, event)
    conn.expire(key, ttl)


# Exclude redis register if unregister is recived
@app.handle("sofia::unregister")
def unregister(event):
    key = "registers:%s" % event["call-id"]
    conn.delete(key)


if __name__ == "__main__":
    # Start Jaspion
    app.run()
