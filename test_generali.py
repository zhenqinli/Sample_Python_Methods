#!/usr/bin/env python3

"""Main driver module for running tests
"""

import os
import sys
import getopt
import datetime


TASK = ''
KPATTERN = ''
FILE_PATH = ''
XDAY = 0
YDAY = 0

def cli():
    """Command-line interface (looks at sys.argv to decide what to do)."""
    class BadUsage(Exception):
        """Print command-line arguments with examples, when help is specified or bad argument is typed"""
        print("Usage: %s -p problem_number -s string -x X -y Y -f FILE_PATH (Problem_number: 1-3)" \
                % sys.argv[0]) 

    # Scripts don't get the current directory in their path by default
    # unless they are run with the '-m' switch
    if '' not in sys.path:
        scriptdir = os.path.dirname(sys.argv[0])
        if scriptdir in sys.path:
            sys.path.remove(scriptdir)
        sys.path.insert(0, '.')

    try:
        # Store input and output file names

        # Read command line args
        myopts, args = getopt.getopt(sys.argv[1:], "P:s:x:y:f:")

        ###############################
        # o == option
        # a == argument passed to the o
        ###############################

        if myopts == []:
            raise BadUsage

        # Loop over command-line options in myopts
        global TASK
        global XDAY
        global YDAY
        global KPATTERN
        global FILE_PATH
        for o, a in myopts:
            if o == '-P':
                if a is not None:
                    print("Problem Number: %s " % a)

                    if a == '1':
                        TASK = a
                    elif a == '2':
                        TASK = a
                    elif a == '3':
                        TASK = a
                    else:
                        raise BadUsage
                else:
                    raise BadUsage

            elif o == '-s':
                KPATTERN = a
                if a is not None:
                    print("key pattern to delete: %s " % a)
                else:
                    raise BadUsage

            elif o == '-x':
                if a is not None:
                    XDAY = int(a)
                    print("X: %s " % a)
                else:
                    raise BadUsage

            elif o == '-y':
                if a is not None:
                    YDAY = int(a)
                    print("Y: %s " % a)
                else:
                    raise BadUsage

            elif o == '-f':
                FILE_PATH = a
                if a is not None:
                    print("JMeter log FILE_PATH: %s " % a)
                else:
                    raise BadUsage

    except(getopt.error, BadUsage):
        os.path.splitext(os.path.basename(sys.argv[0]))[0]
        sys.exit(1)


from lxml import objectify
from lxml import etree
import xml.dom.minidom as mmd
import copy
from datetime import date, timedelta
def check_xml(x,y):
    """Testing XML manipulations."""

    filename = './test_payload1.xml'
    with open(filename, 'r') as f:
        xml=objectify.parse(filename)
        root=xml.getroot()
        root.REQUEST.TP.DEPART = date.today() + timedelta(x)
        root.REQUEST.TP.RETURN = date.today() + timedelta(y)
        xml2=copy.deepcopy(xml)

    out_file = open("output.xml", "w")
    #out_file.write(xml2)
    good_xml = mmd.parseString( str(etree.tostring(xml2))[1:].split("'")[1] )

    print(good_xml.toprettyxml(indent='    ',))
    out_file.write(good_xml.toprettyxml(indent='    ',))


import json
import copy

def check_json(pattern):
    """Testing JSON manipulations."""
    filename = './test_payload.json'
    with open(filename, "r") as input_data_file:
        myjson = input_data_file.read()
        object_j= json.loads(myjson)
        object_j2=copy.deepcopy(object_j)
        for el in object_j:
            if el == pattern:
                object_j2.pop(el,None)
            elif isinstance(object_j[el], dict):
                for c in object_j[el]:
                    if c == pattern:
                        object_j2[el].pop(c, None)
            elif isinstance(object_j[el], list):
                item = 0
                for c in object_j[el]:
                    if c == pattern:
                        object_j2[el].pop(item)
                    item += 1
    out_file = open("output.json", "w")
    print(json.dumps(object_j2))
    out_file.write(json.dumps(object_j2))


from datetime import datetime

def check_jmeter_log(filename):
    """Parsing JMeter Log for non-200 errors."""

    if filename == '':
        filename = './Jmeter_log1.jtl'

    print ("Parsing JMeter log file %s" %(filename))
    with open(filename, "r") as input_data_file:
        lines = input_data_file.readlines()
        for line in lines:
            fields = line.split(',')
            if 'timeStamp' not in line and fields[3] != '200':
                print ("%s, %s, %s, %s, %s\n" \
                        %((datetime.utcfromtimestamp(int(fields[0])/1000-28800).strftime('%Y-%m-%d %H:%M:%S')), fields[2],fields[3],fields[4],fields[8]) )
            elif 'timeStamp' in line:  # print header
                print ("%s, %s, %s, %s, %s\n" \
                        %( fields[0] + ' in PST', fields[2],fields[3],fields[4],fields[8]) )


if __name__ == '__main__':

    cli()
    print ("%s\n" %TASK)
    if TASK == '1':
        check_xml(XDAY,YDAY)
    elif TASK == '2':
        check_json(KPATTERN)
    elif TASK == '3':
        check_jmeter_log(FILE_PATH)
