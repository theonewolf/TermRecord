#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
# jTermReplay.py                                                             #
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



from jinja2 import FileSystemLoader, Template
from jinja2.environment import  Environment

from json import dumps
from math import ceil
from mmap import mmap
from os.path import basename,dirname
from sys import argv



def getTiming(timefname):
    timing = None 
    with open(timefname, 'r') as timef:
        timing = [l.strip().split(' ') for l in timef]
        timing = [(int(ceil(float(r[0]) * 1000)), int(r[1])) for r in timing]
    return timing

def scriptToJSON(scriptfname, timing=None):
    ret = []

    with open(scriptfname, 'rb') as scriptf:
        scriptf.readline() # ignore first header line from script file 
        offset = 0
        for t in timing:
            data = scriptf.read(t[1]).decode('utf-8')
            data = data.replace("'", "\\'") # necessary fixup
            offset += t[0]
            ret.append((data, offset))
    return dumps(ret)

def renderTemplate(json, templatename, outputname=None):
    fsl = FileSystemLoader(dirname(templatename), 'utf-8')
    e = Environment()
    e.loader = fsl

    templatename = basename(templatename)
    rendered = e.get_template(templatename).render(json=json)

    if not outputname:
        return rendered

    with open(outputname, 'w') as outf:
        outf.write(rendered)



if __name__ == '__main__':
    argv        =   dict(enumerate(argv))
    scriptfname =   argv.get(1)
    timefname   =   argv.get(2)
    tmpname     =   argv.get(3) # optional
    outname     =   argv.get(4) # optional
    timing      =   None

    if not scriptfname:
        print 'Script file name needed.'
        exit(1)
    
    if timefname:
        timing = getTiming(timefname)

    json = scriptToJSON(scriptfname, timing)
    if tmpname and outname:
        renderTemplate(json, tmpname, outname)
    elif tmpname:
        print renderTemplate(json, tmpname) 
    else:
        print js
