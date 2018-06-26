#!/usr/bin/env python3
import argparse
import redis
import pickle
import rq
from currency import get_rate


pickle.HIGHEST_PROTOCOL = 2
parser = argparse.ArgumentParser()
parser.add_argument('pairs', type=str, nargs='+')
args = parser.parse_args()

conn = redis.Redis(host='10.0.0.10')
queue = rq.Queue(connection=conn)

jobs = [queue.enqueue(get_rate, pair) for pair in args.pairs]

for job in jobs:
    while job.result is None:
        pass
    print(*job.result)
