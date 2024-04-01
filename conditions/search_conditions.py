import copy

async def provider_search(condition, data):
    res = True
    condition_operator = condition['operator']['value']
    providers_to_be_checked = []

    for field in condition['fields']:
        if field['field_code'] == 'provider':
            providers_to_be_checked = copy.deepcopy(field['values'])
        
    for provider in data['providers']:
        for prv in providers_to_be_checked:
            if condition_operator == "==":
                if prv['value'] == provider['puid']:
                    print("YES MAN")
                    return True
            elif condition_operator == "!=":
                if prv['value'] != provider['puid']:
                    print("YES MAN 1")
                    res = True
                else:
                    res = False
                    return res
    return res

async def dep_airport_search(condition, data):
    res = True
    condition_operator = condition['operator']['value']
    airports_to_be_checked = []

    for field in condition['fields']:
        if field['field_code'] == 'airport':
            airports_to_be_checked = copy.deepcopy(field['values'])

    for direction in data['directions']:
        for dep_airport in airports_to_be_checked:
            if condition_operator == "==":
                if dep_airport['value'] == direction['departure']:
                    print("YES MAN")
                    return True
            elif condition_operator == "!=":
                if dep_airport['value'] != direction['departure']:
                    print("YES MAN 1")
                    res = True
                else:
                    res = False
                    return res
    return res

async def dep_cities_search(condition, data):
    res = True
    condition_operator = condition['operator']['value']
    cities_to_be_checked = []

    for field in condition['fields']:
        if field['field_code'] == 'airport':
            cities_to_be_checked = copy.deepcopy(field['values'])

    for direction in data['directions']:
        for dep_city in cities_to_be_checked:
            if condition_operator == "==":
                if dep_city['value'] == direction['departure']:
                    print("YES MAN")
                    return True
            elif condition_operator == "!=":
                if dep_city['value'] != direction['departure']:
                    print("YES MAN 1")
                    res = True
                else:
                    res = False
                    return res
    return res

async def dep_countries_search(condition, data):
    res = True
    condition_operator = condition['operator']['value']
    countries_to_be_checked = []

    for field in condition['fields']:
        if field['field_code'] == 'airport':
            countries_to_be_checked = copy.deepcopy(field['values'])

    for direction in data['directions']:
        for dep_country in countries_to_be_checked:
            if condition_operator == "==":
                if dep_country['value'] == direction['departure']:
                    print("YES MAN")
                    return True
            elif condition_operator == "!=":
                if dep_country['value'] != direction['departure']:
                    print("YES MAN 1")
                    res = True
                else:
                    res = False
                    return res
    return res