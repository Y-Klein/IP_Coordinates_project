import redis
import json

data = {
    "lat": 31.7674,
    "lon": 35.2186,
}
data2 = {
    "lat": 31.1111,
    "lon": 35.2222,
}

with redis.Redis(host='localhost', port=6365, decode_responses=True) as r:
    # r.set("data2", json.dumps(data))
    # tudent_obj_as_dict = json.loads(r.get("data"))
    # print(tudent_obj_as_dict)
    for key in r.scan_iter("data:"):
        print("!")
        print(key)