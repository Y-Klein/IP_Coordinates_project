import redis

data = {
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
}

with redis.Redis(host='localhost', port=6379, decode_responses=True) as r:
    r.hset('user-session:123', mapping=data)
    print(r.hgetall('user-session:123'))