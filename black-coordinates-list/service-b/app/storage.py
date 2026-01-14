import redis
import json
from schemas import validation

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def writing(ip_json):
    validation(ip_json=ip_json)
    ip_json = {"ip":ip_json["query"],"lat":ip_json["lat"],"lon":ip_json["lon"]}
    r.set(ip_json["ip"], json.dumps(ip_json))


def get_all_ip():
    result = []
    for key in r.keys():
        key_obj_as_dict = json.loads(r.get(f"{key}"))
        result.append(key_obj_as_dict)
    return result


