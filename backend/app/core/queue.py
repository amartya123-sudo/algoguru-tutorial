from redis import Redis
from rq import Queue

redis = Redis(
    host="redis",
    port=6379,
)

execution_queue = Queue(
    "execution",
    connection=redis,
)