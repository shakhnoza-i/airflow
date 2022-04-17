import random
import logging
import requests
import redis
import uuid
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from starlette.requests import Request


app = FastAPI()

r = redis.Redis('192.168.99.100')
logging.basicConfig()


class SearchResult(BaseModel):
    search_id: str
    price: float
    currency: str

    class Meta:
        database = r

"""
- choice one of two services from limited choices
- search in lists(providers) by the index(random number within len(list)) 
of flights in list
- get pricing total field
- get currency field
- lead to a single currency
- order by total pricing

"""
def random_service():
    services = [1,1,1,1,1,2]
    service = random.choice(services)
    return service


@app.post("/search/")
async def create(request: Request):
    req1 = requests.post('http://127.0.0.1:8990/search')
    all_flights = req1.json()
    flight_id = random.randrange(len(all_flights))
    flight = all_flights[flight_id]
    price = flight.get('pricing').get('total')
    currency = flight.get('pricing').get('currency')
    search_id = str(uuid.uuid4())

    search_result = SearchResult(
        search_id = search_id,
        price=price, 
        currency=currency,
    )
    # search_result.save()

    return {"search_id": search_id}
