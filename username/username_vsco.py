#!/usr/bin/env python

import base
import vault
import sys
import requests
from termcolor import colored

# Control whether the module is enabled or not
ENABLED = True


class style:
    BOLD = '\033[1m'
    END = '\033[0m'


def banner():
    print colored(style.BOLD + '\n[+] Checking VSCO.co user details\n' +
                  style.END, 'blue')


def main(username):
    req = requests.get("https://vsco.co/%s/images/1" % username)
    return req.text


def output(data, username=""):
    if username not in data:
        print 'VSCO account does not exist for this username.'
    else:
        print 'VSCO account found at https://vsco.co/%s/images/1' % username
        print '\n-----------------------------\n'

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        banner()
        result = main(username)
        output(result, username)
    except Exception as e:
        print e
        print "Please provide a username as argument"
