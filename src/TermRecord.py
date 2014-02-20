#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
# TermRecord.py                                                              #
#                                                                            #
# This file can either run the 'script' command as a wrapper, or parse its   #
# output with timing information.  It produces self-contained or dynamic     #
# HTML files capable of replaying the terminal session with just a modern    #
# browser.                                                                   #
#                                                                            #
#                                                                            #
#   Authors: Wolfgang Richter <wolf@cs.cmu.edu>                              #
#                                                                            #
#                                                                            #
#   Copyright 2014 Wolfgang Richter and licensed under the MIT License.      #
#                                                                            #
##############################################################################



from argparse import ArgumentParser, FileType
from contextlib import closing
from json import dumps
from math import ceil
from os.path import basename,dirname
from subprocess import Popen
from tempfile import NamedTemporaryFile

from jinja2 import FileSystemLoader, Template
from jinja2.environment import  Environment


# http://blog.taz.net.au/2012/04/09/getting-the-terminal-size-in-python/
def probeDimensions(fd=1):
    """
    Returns height and width of current terminal. First tries to get
    size via termios.TIOCGWINSZ, then from environment. Defaults to 25
    lines x 80 columns if both methods fail.

    :param fd: file descriptor (default: 1=stdout)
    """
    try:
        import fcntl, termios, struct
        hw = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        try:
            hw = (os.environ['LINES'], os.environ['COLUMNS'])
        except:  
            hw = (24, 80)

    return hw

def runScript():
    timingfname = None
    scriptfname = None

    with NamedTemporaryFile(delete=False) as timingf:
        with NamedTemporaryFile(delete=False) as scriptf:
            timingfname = timingf.name 
            scriptfname = scriptf.name

    proc = Popen(['script', '-t%s' % timingfname, scriptfname])
    proc.wait()
    return open(scriptfname, 'r'), open(timingfname, 'r') 

def getTiming(timef):
    timing = None 
    with closing(timef):
        timing = [l.strip().split(' ') for l in timef]
        timing = [(int(ceil(float(r[0]) * 1000)), int(r[1])) for r in timing]
    return timing

def scriptToJSON(scriptf, timing=None):
    ret = []

    with closing(scriptf):
        scriptf.readline() # ignore first header line from script file 
        offset = 0
        for t in timing:
            data = scriptf.read(t[1]).decode('utf-8')
            data = data.replace("'", "\\'") # necessary fixup
            offset += t[0]
            ret.append((data, offset))
    return dumps(ret)

def renderTemplate(json, dimensions, templatename, outfname=None):
    fsl = FileSystemLoader(dirname(templatename), 'utf-8')
    e = Environment()
    e.loader = fsl

    templatename = basename(templatename)
    rendered = e.get_template(templatename).render(json=json,
                                                   dimensions=dimensions)

    if not outf:
        return rendered

    with closing(outf):
        outf.write(rendered)



if __name__ == '__main__':
    argparser   =   ArgumentParser(description=
                                        'Stores terminal sessions into HTML.')

    argparser.add_argument('-s', '--script-file', type=FileType('r'),
                           help='script file to parse', required=False)
    argparser.add_argument('-t', '--timing-file', type=FileType('r'),
                           help='timing file to parse', required=False)
    argparser.add_argument('-m', '--template-file', type=str,
                           help='file to use as HTML template', required=False)
    argparser.add_argument('-o', '--output-file', type=FileType('w'),
                           help='file to output HTML to', required=False)

    ns = argparser.parse_args()

    scriptf     =   ns.script_file
    timef       =   ns.timing_file 
    tmpname     =   ns.template_file # optional
    outf        =   ns.output_file   # optional

    if (scriptf and not timef) or (timef and not scriptf):
        parser.error('Both SCRIPT_FILE and TIMING_FILE have to be specified' +
                     'together.')
        exit(1)
   
    dimensions = probeDimensions() if not scriptf else (24,80)

    if not scriptf:
        scriptf,timef = runScript()

    timing = getTiming(timef)
    json = scriptToJSON(scriptf, timing)
    if tmpname and outf:
        renderTemplate(json, dimensions, tmpname, outf)
    elif tmpname:
        print renderTemplate(json, tmpname) 
    else:
        print json
