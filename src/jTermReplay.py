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
TEMPLATE    = 'term.write(\'%s\');\n'


def getTiming(timefname):
    timing = None 
    with open(timefname, 'r') as timef:
        timing = [l.strip().split(' ') for l in timef]
        timing = [(int(ceil(float(r[0]) * 1000)), int(r[1])) for r in timing]
    return timing    

def scriptToJS(scriptfname, timing=None):
    ret = HEADER

    with open(scriptfname, 'r+b') as scriptf:
        mm = mmap(scriptf.fileno(), 0)
        head = mm.readline() # ignore first header line from script file 
        pos = len(head)
        for t in timing:
            ret += TEMPLATE % (mm[pos : pos + t[1]].encode('string-escape'))
            pos += t[1]
        mm.close()
    
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
