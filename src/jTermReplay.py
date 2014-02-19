#!/usr/bin/env python



from math import ceil
from mmap import mmap
from sys import argv



HEADER      = r'''window.addEventListener('load', function() {
    var term = new Terminal({
        cols: 80,
        rows: 30,
        screenKeys: true
    });

    term.open(document.body);
    term.write('\x1b[31m--- Replaying Script ---\x1b[m\r\n');
'''
FOOTER      = r'''}, false);'''
TEMPLATE    = 'setTimeout(function() {term.write(\'%s\');}, %d);\n'


def getTiming(timefname):
    timing = None 
    with open(timefname, 'r') as timef:
        timing = [l.strip().split(' ') for l in timef]
        timing = [(int(ceil(float(r[0]) * 1000)), int(r[1])) for r in timing]
    return timing    

def scriptToJS(scriptfname, timing=None):
    ret = HEADER

    with open(scriptfname, 'rb') as scriptf:
        scriptf.readline() # ignore first header line from script file 
        offset = 0
        for t in timing:
            data = scriptf.read(t[1]).decode('utf-8').encode('unicode-escape')
            data = data.replace("'", "\\'") # odd fixup
            offset += t[0]
            ret += TEMPLATE % (data, offset)
    
    ret += FOOTER
    return ret



if __name__ == '__main__':
    argv        =   dict(enumerate(argv))
    scriptfname =   argv.get(1)
    timefname   =   argv.get(2)
    timing      =   None

    if not scriptfname:
        print 'Script file name needed.'
        exit(1)
    
    if timefname:
        timing = getTiming(timefname)

    js = scriptToJS(scriptfname, timing)
    print js
