import time

import requests


while True:
    requests.get('http://localhost:8000')
    time.sleep(.2)
