from fastapi import APIRouter
from config.db import conn
from models.index import orders
from schemas.index import Order
order = APIRouter()

@order.get("/")
async def read_data():
    return conn.execute(orders.select()).fetchall()

@order.get("/{order_id}")
async def read_data(order_id: int):
    return conn.execute(orders.select().where(orders.c.order_id == order_id)).fetchall()

@order.post("/")
async def write_data(order: Order):
    conn.execute(orders.insert().values(
        order_description=order.order_description,
        order_status=order.order_status,
        last_updated_timestamp=order.last_updated_timestamp,
        special_order=order.special_order))
    return conn.execute(orders.select()).fetchall()

@order.put("/{order_id}")
async def update_data(order_id: int, order: Order):
    conn.execute(orders.update().values(
        order_description=order.order_description,
        order_status=order.order_status,
        last_updated_timestamp=order.last_updated_timestamp,
        special_order=order.special_order).where(orders.c.order_id == order_id)),
    return conn.execute(orders.select()).fetchall()

@order.delete("/{order_id}")
async def delete_data(order_id: int):
    conn.execute(orders.delete().where(orders.c.order_id == order_id))
    return conn.execute(orders.select()).fetchall()