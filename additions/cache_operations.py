import os
import redis
import json

from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

HOST = "localhost" # os.getenv('CACHE_HOST')
PORT = 6379 # os.getenv('CACHE_PORT')

MINUTES = 11

async def set_after_rules(rules, request_id):
    key = f"after_rules_{request_id}"

    data = {
        "after_rules": rules
    }

    redis_client = redis.Redis(host=HOST, port=PORT)
    redis_client.set(
        key,
        json.dumps(data), 
        MINUTES*60  
    )
    redis_client.close()

async def get_after_rules(request_id):
    key = f"after_rules_{request_id}"
    # print("get rules", key)
    # print(HOST, PORT)
    redis_client = redis.Redis(host=HOST, port=str(PORT)) 

    rules = redis_client.get(key) 
    redis_client.close()
    # print(rules)

    return rules['after_rules'] if rules is not None else None

