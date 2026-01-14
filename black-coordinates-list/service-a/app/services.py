import requests


SERVICE_B_URL = "http://127.0.0.1:8001/"
IP_API_URL = "http://ip-api.com/json/"


def get_coordinates(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?fields=query,lat,lon", timeout=5)

    data = response.json()
    return data


def send_to_service_b(coordinates: dict):
    response = requests.post(
        f"{SERVICE_B_URL}/coordinates",
        json=coordinates,
        timeout=5
    )

    if not response.ok:
        raise Exception("failed to send data to service B")

    return response.json()

def resolve_ip_and_send(ip: str):
    coordinates = get_coordinates(ip)
    data = send_to_service_b(coordinates)
    return data
