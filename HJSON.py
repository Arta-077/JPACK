"""
This package helps you to have faster programming in reading and writing json files.
"""

# Edited: 1404/06/27 , 11:49
# P: توضیحات  توابع ناقصه تکمیل کن

import json
import requests


# ......READ......
def READ_file(Link=str):
    """
    This function read json file.
    """
    try:
        with open(Link, "r", encoding="utf-8") as F:
            DATA = json.load(F)

        return DATA

    except Exception as e:
        print("Error! File not found.")
        print(f"your error is: {e} \n")


def READdata_yielder(DATA):
    """
    Pass
    """
    for KEY, VALUE in DATA.items():
        yield (KEY, VALUE)


def READ_requests(Address_Link):
    """
    Pass
    """
    response = requests.get(Address_Link)
    json_data = response.json()
    # print(json_data)
    KEY, VALUE = READdata_yielder(json_data)
    return KEY, VALUE


# ......SHOW......
def SHOW_file(Link=str):
    """
    This function show key and value from json file.
    """
    DATA = READ_file(Link)

    for KEY, VALUE in DATA.items():
        print(f"KEY: {KEY}  VALUE: {VALUE}")


def SHOW_data(DATA, custom=False, key_name=None, value_name=None):
    """
    This function show key and value in your valuable.
    """
    if custom == True:
        for KEY, VALUE in DATA.items():
            print(f"{key_name}: {KEY}  {value_name}: {VALUE}")
    else:
        for KEY, VALUE in DATA.items():
            print(f"KEY: {KEY}  VALUE: {VALUE}")


# ......WRITE......
def WRITE_LoadUpdate(Link, KEY, VALUE):
    """
    This function takes and write one key value and load last data in json file and updated.
    """
    dict_cache = dict()
    dict_cache.setdefault(KEY, VALUE)
    # print(dict_cache)

    with open(Link, "r", encoding="utf-8") as F:
        DATA = json.load(F)

        dict_cache.update(DATA)

    if KEY in dict_cache:
        dict_cache[KEY] = VALUE

    with open(Link, "w", encoding="utf-8") as F:
        json.dump(dict_cache, F, indent=4, ensure_ascii=False)


def WRITE_dict(Link, DICT):
    """
    This function takes dictionary and write into json file.
    """
    dict_cache = dict()
    dict_cache.update(DICT)

    with open(Link, "w", encoding="utf-8") as F:
        json.dump(dict_cache, F, indent=4, ensure_ascii=False)


def WRITE_kwargs(Link, **kwargs):
    """
    This function takes kwargs and write into json file.
    """
    dict_cache = dict()
    dict_cache.update(**kwargs)

    with open(Link, "w", encoding="utf-8") as F:
        json.dump(dict_cache, F, indent=4, ensure_ascii=False)


# ......NAME......
if __name__ == "__main__":
    print("hey body, use this package in your program.")
