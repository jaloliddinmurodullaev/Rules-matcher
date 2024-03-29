import os
import json
import asyncio
import uuid

from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import Request

from additions.asyncrequest import offers_request_to_content

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '../.env'))
RULES_URL = os.environ.get("RULES_URL")
CONTENT_URL = os.environ.get("CONTENT_URL")

router = APIRouter(
    prefix='/offers',
    tags=['content']
)

# offers handler to get flight offers that are searched before and applying user rules
@router.post("/")
async def offers(request: Request):
    body = await request.json()
    print("CONTENT URL : ", CONTENT_URL if CONTENT_URL is not None else "Rizo-oy")
    offerResponse = await offers_request_to_content(url=CONTENT_URL + '/content/offers', context=json.dumps(body))
    return offerResponse