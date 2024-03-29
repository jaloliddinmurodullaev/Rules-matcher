import os
from fastapi import FastAPI
from handlers import urls

app = FastAPI(title="Rules matcher API", 
              version="1.0",
              description="Rules matcher module that applies all rules to Content microservice"
            )

app.include_router(urls.router)






