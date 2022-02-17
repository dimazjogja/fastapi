from construct import Bit, Timestamp
from numpy import datetime64
from pydantic import BaseModel

class Order(BaseModel):
    order_description: str
    order_status: str
    last_updated_timestamp: int
    special_order: bool
    
    