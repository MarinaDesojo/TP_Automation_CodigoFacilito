import time
import requests
from API_project.utils.settings import BASE_URL, AIRPORTS, USERS, fake

RETRIES = 3

def api_request(method, path, **kwargs):
    url = f"{BASE_URL}{path}"
    for i in range(RETRIES):
        resp = requests.request(method, url, timeout=5, **kwargs)
        if resp.status_code < 500 or i == RETRIES-1:
            try:
                resp.raise_for_status()
            except:
                try:
                    print(f"Response: {resp.text}")
                except:
                    pass
            return resp
        time.sleep(5) #valor que retorna i que sea menor que la cantidad de intentos, aunque no es una buena practica


def requests_with_error_handling(**kwargs):
    r = requests.request(**kwargs)
    try:
        r.raise_for_status()
    except Exception as e:
        try:
            print(f"Response: {r.text}")
        except:
            pass
        raise e
    return r







class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"} if token else {}

    def get(self, path, **kwargs):
        return requests.get(f"{self.base_url}{path}", headers=self.headers, **kwargs)

    def post(self, path, **kwargs):
        return requests.post(f"{self.base_url}{path}", headers=self.headers, **kwargs)

    # Otros métodos: put, delete...