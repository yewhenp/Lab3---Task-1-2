"""
Module for navigating into twitter json
"""

import json

def get_json(address):
    """
    str -> dict/list
    This func reads json
    """
    file = open(address)

    return json.loads(file.read())


def get_elem_dict(json_layer):
    """
    dict -> obj
    This func returns chosen elem of json on the current layer
    """
    list_of_keys = list(json_layer.keys())

    print("Please, enter a number of interested obj")

    for number in range(1, len(list_of_keys) + 1):
        print(number, "---", list_of_keys[number - 1])

    print()
    number = int(input()) - 1

    return json_layer[list_of_keys[number]]


def get_elem_list(json_layer):
    """
    dict -> obj
    This func returns chosen elem of json on the current layer
    """
    print("Please, enter a index number (your obj is list)")
    print("There are", len(json_layer), "objects in list")

    print()
    number = int(input()) - 1

    return json_layer[number]


def main():
    """
    None -> None
    Main func
    """
    address = input("Please, enter a path to file: ")

    json_layer = get_json(address)

    while str(type(json_layer)) == "<class 'dict'>" or str(type(json_layer)) == "<class 'list'>":
        try:
            json_layer = get_elem_dict(json_layer)
        except AttributeError:
            json_layer = get_elem_list(json_layer)

    print("Your value is:", json_layer)


if __name__ == '__main__':
    main()
