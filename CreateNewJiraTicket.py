#!/usr/bin/python

from __future__ import print_function
import sys
import json
import argparse
import pycurl
import base64

def addNewIssue(opts):
    '''
    Send the request to open a new issue with the date of next Tuesday
    and set-up headers with basic authentication and Accept this headers are required
    '''
    try:
        url = '%s/rest/api/2/issue/' % opts.server
        pycurl_connect = pycurl.Curl()
        pycurl_connect.setopt(pycurl.POST, 1)
        pycurl_connect.setopt(pycurl.URL, url)
        pycurl_connect.setopt(pycurl.HTTPHEADER, ['Authorization:Basic %s' % base64.b64encode("admin:admin"),
                                                "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                                "Content-Type: application/json"])

        pycurl_connect.setopt(pycurl.POSTFIELDS, opts.data)
        pycurl_connect.perform()

    except pycurl.error, error:
        errno, errstr = error
        print ('An error occurred: %s' % errstr)

def parseArgs():
    '''
    Parse the user inputs like project name, server etc
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', action='store', help='Project to fetch the sprint update for' )
    parser.add_argument('--server', action='store', help='Server to query')
    parser.set_defaults( server='https://kdavawala.atlassian.net', project='DEV' )

    opts = parser.parse_args()
    return opts;

def main():
    '''
    Parse the args and the data, call the add new ticket function
    '''
    opts = parseArgs()
    opts.data = "{\"fields\":{\"project\":{\"id\":\"10000\"},\"summary\":\"Sprint Ticket\","
    opts.data += "\"description\":\"Ola camosta\","
    opts.data += "\"issuetype\":{\"name\":\"Task\"}}}"
    addNewIssue(opts)

if __name__ == '__main__':
    rc = 0
    try:
        main()
    except NameError as e:
        print("Unexpected error:", e)
        rc = -1

    exit( rc )
