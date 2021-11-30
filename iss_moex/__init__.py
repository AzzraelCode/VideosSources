import pandas as pd
pd.set_option("display.max_columns", 15)

import json
import requests

from urllib import parse
from config import get_path


def query(method : str, **kwargs):
    """
    Отправляю запрос к ISS MOEX
    :param method:
    :param kwargs:
    :return:
    """
    try:
        url = "https://iss.moex.com/iss/%s.json" % method
        if kwargs: url += "?" + parse.urlencode(kwargs)
        r = requests.get(url)
        r.encoding = 'utf-8'
        j = r.json()
        return j

    except Exception as e:
        print("query error %s" % str(e))
        return None

def flatten(j:dict, blockname:str):
    """
    Собираю двумерный массив (словарь)
    :param j:
    :param blockname:
    :return:
    """
    return [{k : r[i] for i, k in enumerate(j[blockname]['columns'])} for r in j[blockname]['data']]

def main():
    print("I'm %s at %s" % (__name__, get_path(__name__)))

    # Список бумаг торгуемых на московской бирже
    # https://iss.moex.com/iss/reference/5
    # j = query("securities")
    # j = query("securities", q="сбер")
    # j = query("securities", group_by="type", group_by_filter="corporate_bond", limit=10)
    j = query("securities", q="втб", group_by="type", group_by_filter="corporate_bond", limit=10)
    f = flatten(j, 'securities')

    # Спецификация инструмента
    # https://iss.moex.com/iss/reference/13
    # secid = 'RU000A102QJ7'
    # method = "securities/%s" % secid
    # j = query(method)
    # f = flatten(j, 'description')

    # Купоны по облигациям
    # ** описания нет
    # secid = 'RU000A102QJ7'
    # method = "securities/%s/bondization" % secid
    # j = query(method)
    # f = flatten(j, 'coupons')

    # Дивиденды по акциям
    # ** описания нет
    # secid = 'MTSS'
    # method = "securities/%s/dividends" % secid
    # j = query(method)
    # f = flatten(j, 'dividends')

    print(pd.DataFrame(f))
    # print(pd.DataFrame(f, columns=['secid','shortname' ,'primary_boardid', 'type']))
    # print(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=True))