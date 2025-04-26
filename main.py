import logging
from typing import Optional
from fastapi import FastAPI


logging.basicConfig(filename='api_logs.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')

app = FastAPI()
