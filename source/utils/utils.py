import math
import random
from sqlalchemy.inspection import inspect
from source.database import connect
from collections import defaultdict
from io import BytesIO
import pandas as pd
from flask import send_file
from datetime import datetime
import logging
from source.helpers.s3 import S3Helper
from source.commons import environment
import requests

OUTPUT_PATH = '/tmp'

def build_result(data, command, order_by):
    records = 0
    per_page = 20
    if data.get('page'):
        result = connect().execute(command, skip_load_query=True).fetch_all() # database.engine.execute(text(command)).fetchall()
        records = len(result)

        command = command + order_by

        page = data["page"] - 1 if data["page"] > 0 else data['page']
        per_page = data["per_page"]
        if data["page"] == 1:
            command = command + f" offset {page} "
        else:
            page = ((per_page * data["page"]) - per_page)
            command = command + f" offset {page} "

        if data["per_page"] > 0:
            command = command + f" limit {data['per_page']} "
            per_page = data["per_page"]
        else:
            return [], 0, 0

        result = connect().execute(command, skip_load_query=True).fetch_all() #database.engine.execute(text(command)).fetchall()
        return result, records, math.ceil(records / per_page)

    command = command + order_by

    result = connect().execute(command, skip_load_query=True).fetch_all() #database.engine.execute(text(command)).fetchall()
    return result, records, math.ceil(records / per_page)


def get_param_by_name(name):
    command = f"""
                select *
                from parameter c
                where   c.name = '{name}'
                """

    result = connect().execute(command, skip_load_query=True).fetch_all() #database.engine.execute(text(command)).fetchall()
    return result
