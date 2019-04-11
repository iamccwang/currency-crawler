# -*- coding: utf-8 -*-
import copy
import os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv, find_dotenv

class connect_database:
    def insert (self, data):
        list_units = list(data["rates"].keys())

        default_unit = list_units[0]
        sorted_data = copy.deepcopy(data)
        sorted_data["unit"] = default_unit
        sorted_data["rates"] = data["rates"][default_unit]
        sorted_data["modified_times"] = 0
        sorted_data["last_modified"] = datetime.utcnow()

        query_data = { "base": sorted_data["base"], "unit": default_unit, "date": sorted_data["date"] }
        found_data = self.collection.find(query_data)

        if found_data.count() is 0:
            self.collection.insert_one(sorted_data);
        else:
            self.collection.update_one(query_data, { "$inc": {"modified_times": 1}, "$set": {"rates": sorted_data["rates"], "last_modified": sorted_data["last_modified"]} });

    def __init__ (self):
        load_dotenv(find_dotenv());
        self.client = MongoClient(os.getenv("DATABASE_CONNECTION"))
        self.collection = self.client[os.getenv("DATABASE")][os.getenv("COLLECTION")]