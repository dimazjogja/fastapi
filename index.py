from fastapi import FastAPI
from routes.index import order

app = FastAPI(title="/processOrder()")
app.include_router(order)

