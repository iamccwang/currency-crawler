# -*- coding: utf-8 -*-
import os
import requests
from dotenv import load_dotenv, find_dotenv

def get (base, symbol):
    url = os.getenv("API_URL").format(base=base, symbol=symbol)
    res = requests.get(url)
    return res
