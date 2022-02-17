from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, TIMESTAMP
from config.db import meta
orders = Table(
    'orders', meta, 
    Column('order_id', Integer, primary_key=True),
    Column('order_description', String(255)),
    Column('order_status', String(255)),
    Column('last_updated_timestamp', Integer),
    Column('special_order', Boolean)
    )