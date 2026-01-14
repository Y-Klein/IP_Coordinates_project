from pydantic import TypeAdapter,IPvAnyAddress,ValidationError
from typing_extensions import TypedDict




class Validation(TypedDict):
    query:IPvAnyAddress
    lat:float
    lon:float

valid = TypeAdapter(Validation)



def validation(ip_json):
     valid.validate_python(dict(ip_json))





