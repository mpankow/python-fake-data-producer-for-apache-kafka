from faker.providers import BaseProvider
from yahoo_fin import stock_info as si
import random
import json
import time
from datetime import datetime
import uuid


StockNames = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "DOGE-USD"]


class RealStockProvider(BaseProvider):
    def stock_name(self):
        return random.choice(StockNames)

    def stock_value(self, stockname):
        nextval = si.get_live_price(stockname)
        return nextval

    def produce_msg(self):
        random_id = str(uuid.uuid4())
        stockname = self.stock_name()
        timestamp_ms = int(time.time() * 1000) #current timestamp in ms
        datetime_obj = datetime.fromtimestamp(timestamp_ms / 1000) #convert timestamp to datetime
        iso_8601_timestamp = datetime_obj.isoformat() #format datetime in iso format
        
        message = {
            "stock_name": stockname,
            "stock_value": self.stock_value(stockname),
            "event_time": timestamp_ms,
            "iso_date": iso_8601_timestamp,
        }
        key = {"id": random_id}
        
        return message, key

