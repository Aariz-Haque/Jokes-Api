import json
import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    with open('wocka.json', 'r') as f:
        data = json.load(f)
    
    random_joke=random.choice(data)
    return random_joke
@app.get("/{category}")
def read_root(category:str):
    with open('wocka.json', 'r') as f:
        data = json.load(f)
    category_joke=[item for item in data if item['category'].replace(" ","").lower() == category]
    random_joke=random.choice(category_joke)
    return random_joke
