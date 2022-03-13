import os
import tempfile
import json
import argparse


def get_data():
    if os.path.exists(os.path.join(tempfile.gettempdir(), 'storage.data')):
        with open(os.path.join(tempfile.gettempdir(), 'storage.data'), 'r', encoding='utf8') as f:
            json_data = json.load(f)
            return json_data
    else:
        print('No data file')


def put_data(data_dict):
    with open(os.path.join(tempfile.gettempdir(), 'storage.data'), 'w', encoding='utf8') as f:
        json.dump(data_dict, f)


def val_add(key, value):
    data = get_data() or dict()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    put_data(data)


def val_get(key):
    data = get_data()
    if (data is not None) and (key in data):
        print(*data[key], sep=', ')
        return data[key]
    else:
        print(None)
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')
    parser.add_argument('-v', '--val')
    args = parser.parse_args()
    key = args.key
    value = args.val

    if key and value:
        val_add(key, value)
    elif key:
        val_get(key)
