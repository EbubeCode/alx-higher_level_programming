#!/usr/bin/python3
"""load and save from json"""
import json
import sys
load_jf = __import__('6-load_from_json_file').load_from_json_file
save_jf = __import__('5-save_to_json_file').save_to_json_file


def main():
    """main method"""
    o_list = []
    try:
        f = open('add_item.json', 'r', encoding='UTF-8')
        o_list = json.load(f)
        f.close()
    except Exception:
        pass
    with open('add_item.json', 'w', encoding='UTF-8') as f:
        n_list = sys.argv[1:]
        o_list += n_list
        json.dump(o_list, f)


if __name__ == '__main__':
    main()
