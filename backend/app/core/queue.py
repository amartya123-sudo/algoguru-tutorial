from redis import Redis
from rq import Queue

redis = Redis(
    host="localhost",
    port=6379,
)

execution_queue = Queue(
    "execution",
    connection=redis,
)