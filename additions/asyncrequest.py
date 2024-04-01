import aiohttp

# Do no change the function as it is one of the main methods
async def send_get_request(url, headers, params, context):
    async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, data=context, params=params) as response:
                status_code = response.status
                try:
                    result = await response.json()
                except:
                    result = await response.text()
                return [status_code, result]
            
# Do no change the function as it is one of the main methods
async def send_post_request(url, headers, params, context):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=context, params=params) as response:
            status_code = response.status
            try:
                result = await response.json()
            except:
                result = await response.text()
            return [status_code, result]


# WRITE DOWN ALL OF YOUR ASYNCRONOUS REQ/RES FUNCTIONS
        
# This function is for getting user rules
async def get_user_rules(url, headers=None, params=None, context=None):
    userRules = await send_get_request(url=url, headers=headers, params=params, context=context)
    return userRules[1]

# This function is for searching available tickets
async def search_request_to_content(url, headers=None, params=None, context=None):
    searchResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return searchResponse[1]

# This function is for getting available tickets
async def offers_request_to_content(url, headers=None, params=None, context=None):
    offersResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return offersResponse[1]

# This function is for getting available tickets' fare families
async def upsell_request_to_content(url, headers=None, params=None, context=None):
    upsellResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return upsellResponse[1]

# This function is for getting available ticket's rules
async def rules_request_to_content(url, headers=None, params=None, context=None):
    rulesResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return rulesResponse[1]

# This function is to verify an available ticket
async def verify_request_to_content(url, headers=None, params=None, context=None):
    verifyResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return verifyResponse[1]

# This function is to book an available ticket
async def booking_request_to_content(url, headers=None, params=None, context=None):
    bookingResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return bookingResponse[1]

# This function is to cancel a booked ticket
async def cancel_request_to_content(url, headers=None, params=None, context=None):
    cancelResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return cancelResponse[1]

# This function is to ticket a booked ticket
async def ticket_request_to_content(url, headers=None, params=None, context=None):
    ticketResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return ticketResponse[1]

# This function is to void a confirmed ticket
async def void_request_to_content(url, headers=None, params=None, context=None):
    voidResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return voidResponse[1]

# This function is to refund
async def refund_request_to_content(url, headers=None, params=None, context=None):
    refundResponse = await send_post_request(url=url, headers=headers, params=params, context=context)
    return refundResponse[1]


