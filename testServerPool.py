#!/usr/bin/env python

import argparse
import httplib
import logging
from colorama import init
init()
from colorama import Fore

OPTS=None

def process_args():
    """ process the cli arguments"""

    parser = argparse.ArgumentParser(description="Server pool response testing")

    parser.add_argument('hosts', metavar='host', nargs='+', help='List of hostnames to check')
    parser.add_argument('--version', action='version', version="%(prog)s Brian Wigginton <brianwigginton@gmail.com>")
    parser.add_argument('-p', '--path', default='/', help="target path to check");
    parser.add_argument('-s', '--secure', help="Use HTTPS", action='store_true');
    parser.add_argument('-v', '--verbose', help="set verbosity", action='store_true')
    parser.add_argument('-d', '--debug', help="debug", action='store_true');

    global OPTS
    OPTS = parser.parse_args()

    if(OPTS.debug): logging.basicConfig(level=logging.DEBUG)


def main():
    process_args()

    for server in OPTS.hosts:

        protocol = None
        if OPTS.secure:
            protocol = 'https://'
            conn = httplib.HTTPSConnection(server)
        else:
            protocol = 'http://'
            conn = httplib.HTTPConnection(server)

        target = protocol+server+OPTS.path

        conn.request("HEAD", OPTS.path)
        r = conn.getresponse()

        status = str(r.status) + " " + r.reason

        if status.startswith("2"):
            status = Fore.GREEN + status + Fore.RESET
        else:
            status = Fore.RED + status + Fore.RESET

        print target, status
        #print"\n\t".join(header[0] + ": " + header[1] for header in r.getheaders())

if(__name__ == "__main__"):
    main()
