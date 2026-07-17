from redis import Redis
from rq import Worker, Queue

redis = Redis(
    host="redis",
    port=6379,
)

queue = Queue(
    "execution",
    connection=redis,
)

worker = Worker(
    [queue],
    connection=redis,
)

if __name__ == "__main__":
    worker.work()