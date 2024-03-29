import os
import json
import asyncio
import uuid

from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import Request

from additions.asyncrequest import search_request_to_content

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '../.env'))
RULES_URL = os.environ.get("RULES_URL")
CONTENT_URL = os.environ.get("CONTENT_URL")

router = APIRouter(
    prefix='/search',
    tags=['content']
)

# search handler to handle user rules and search for offers
@router.post('/')
async def search(request: Request):
    body = await request.json()
    print("CONTENT URL : ", CONTENT_URL if CONTENT_URL is not None else "Rizo-oy")
    searchResponse = await search_request_to_content(url=CONTENT_URL + '/content/search', context=json.dumps(body))
    print(searchResponse)
    return searchResponse
