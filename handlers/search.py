import os
import json
import asyncio
import uuid
import copy

from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import Request

from additions.asyncrequest import get_user_rules
from additions.asyncrequest import search_request_to_content

from conditions.search_conditions import SearchEvents

from conditions.search_conditions import provider_search
from conditions.search_conditions import dep_airport_search
from conditions.search_conditions import dep_cities_search
from conditions.search_conditions import dep_countries_search


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

    rules = await get_user_rules(url=RULES_URL)
    if rules['status'] != "success":
        return {
            "status": "error",
            "code": 409,
            "request_id": None,
            "errors": ['User rules has not been found. In this case, you cannot search for flights']
        }
    print("Body before rules: ", body)
    print("Rules status: ", rules['status'])
    rules = rules['data']['rules']
    print(rules)
    body = copy.deepcopy(await filter_request_data(data=body, rules=rules))
    print("Body after rules: ", body)
    print("CONTENT URL : ", CONTENT_URL if CONTENT_URL is not None else "Rizo-oy")
    searchResponse = await search_request_to_content(url=CONTENT_URL + '/content/search', context=json.dumps(body))
    print(searchResponse)
    return searchResponse


async def filter_request_data(data, rules):
    new_data = copy.deepcopy(data)

    for rule in rules:
        if rule['status'] == 'A':
            print("BU YERGA KIRMASLIGI KERAK AGAR STATUS L BOLSA")
            operator = '-'
            if 'and' in rule['rule']:
                operator = 'and'
            if 'or' in rule['rule']:
                operator = 'or'
        
            if await conditions(conditions=rule['conditions_data'], operator=operator, data=data):
                new_data = copy.deepcopy(await operations(data=new_data, operations=rule['operations_data']))
            else:
                new_data = copy.deepcopy(await otherwise_operations(data=new_data, operations=rule['otherwise_operations_data']))
                
    return new_data

async def conditions(conditions, operator, data):
    will_condition_be_used = True

    if operator == 'and':
        for cond in conditions:
            if cond['event_data']['event_code'] == 'provider_search':
                ps = SearchEvents(condition=cond, data=data)
                will_condition_be_used = will_condition_be_used and await ps.provider_search()
            elif cond['event_data']['event_code'] == 'dep_airports_search':
                ps = SearchEvents(condition=cond, data=data)
                will_condition_be_used = will_condition_be_used and await ps.dep_airport_search()
            else:
                print('Condition did not match')
                pass
    elif operator == 'or':
        for cond in conditions:
            if cond['event_data']['event_code'] == 'provider_search':
                print("True")
                if await provider_search(condition=cond, data=data):
                    will_condition_be_used = True
                    return will_condition_be_used
                else:
                    will_condition_be_used = False
            elif cond['event_data']['event_code'] == 'dep_airports_search':
                print("True")
                if await dep_airport_search(condition=cond, data=data):
                    will_condition_be_used = True
                    return will_condition_be_used
                else:
                    will_condition_be_used = False
    else:
        for cond in conditions:
            if cond['event_data']['event_code'] == 'provider_search':
                print(True)
                return await provider_search(condition=cond, data=data)
            if cond['event_data']['event_code'] == 'dep_airports_search':
                print(True)
                return await dep_airport_search(condition=cond, data=data)
    
    return will_condition_be_used


async def operations(data, operations):
    res_data = copy.deepcopy(data)

    for operation in operations:
        new_data = copy.deepcopy(res_data)
        print(operation)
        if operation['action_data']['action_code'] == 'turn_off_provider_search':
            new_data['providers'] = []
            provider_list_to_be_turned_off = []
            for field in operation['fields']:
                if field['field_code'] == 'provider':
                    provider_list_to_be_turned_off = copy.deepcopy(field['values'])
                    break
            for prv in data['providers']:
                is_provider_in_disabled_mode = False
                for provider in provider_list_to_be_turned_off:
                    if provider['value'] == prv['puid']:
                        is_provider_in_disabled_mode = True
                        break
                print("is_provider_in_disabled_mode: ", is_provider_in_disabled_mode)
                if not is_provider_in_disabled_mode:
                    new_data['providers'].append(prv)
            res_data = copy.deepcopy(new_data)
        elif operation['action_data']['action_code'] == 'turn_off_providers':
            new_data['providers'] = []
            res_data = copy.deepcopy(new_data)

    return res_data


async def otherwise_operations(data, operations):
    return data