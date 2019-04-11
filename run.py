# -*- coding: utf-8 -*-
import requests
from database import database
from currency_api import currency_api

connectedDB = database.connect_database();
res = currency_api.get("USD", "AUD");

if not res.status_code == requests.codes.ok:
    res.raise_for_status()    
else:
    connectedDB.insert(res.json());