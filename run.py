# -*- coding: utf-8 -*-
import requests
import sys
from database import database
from currency_api import currency_api

if len(sys.argv) < 3:
    sys.exit()

currency_you_have = sys.argv[1]
currency_you_want = sys.argv[2]

connectedDB = database.connect_database();
res = currency_api.get(currency_you_have, currency_you_want);

if not res.status_code == requests.codes.ok:
    res.raise_for_status()    
else:
    connectedDB.insert(res.json());