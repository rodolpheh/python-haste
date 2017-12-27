#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import argparse

address = "http://127.0.0.1:7777"

class Haste(object):

    def __init__(self, data, key, address):
        super(Haste, self).__init__()
        self.data = data
        self.key = key
        self.raw = address + "/raw/" + self.key
        self.address = address + "/" + self.key

    @classmethod
    def add(cls, data, address):
        if len(data.encode('utf-8')) > 524288:
            print("Data size exceed the maximum size (512kiB), not sending.")
            return None

        try:
            haste = requests.post(address + "/documents", data)
        except requests.ConnectionError as error:
            print(error)
            return None

        return cls(data, haste.json()["key"], address)

    @classmethod
    def get(cls, key, address):
        if len(key) != 10:
            print("Not a valid key")
            return None

        try:
            haste = requests.get(address + "/raw/" + key)
        except requests.ConnectionError as error:
            print(error)
            return None
        return cls(haste.text, key, address)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload the content of a file to an hastebin server')
    parser.add_argument('file', metavar='<file>', help='The file to upload', nargs="?")
    parser.add_argument('--raw', dest='raw', action='store_true', help='Return raw URL (default disabled)')
    parser.add_argument('--address', dest='address', help="Address of the hastebin server (with port if necessary)")
    parser.add_argument('--get', dest='key', help="Get the raw content of an haste", metavar='key')
    args = parser.parse_args()

    address = address if args.address is None else args.address

    if args.key is not None:
        print("Retrieving haste")
        haste = Haste.get(args.key, address)
        if haste == None:
            print("An error occured")
        else:
            print(haste.data)
    else:
        if args.file is not None:
            with open(args.file, 'r') as file:
                data = "".join(file.readlines()).strip()
        else:
            data = "".join(sys.stdin.readlines()).strip()
        haste = Haste.add(data=data, address=address)
        if haste == None:
            print("An error occurred")
        else:
            print(haste.raw if args.raw else haste.address)
