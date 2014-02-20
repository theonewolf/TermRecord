# TermRecord

## Installation

```python
sudo pip install TermRecord
TermRecord -m /usr/share/TermRecord/templates/static.jinja2 -o session-static.html```

## Usage

There are three main modes of operation: (1) wrap the `script` program and dump
JSON to stdout, (2) wrap the `script` program and dump HTML to stdout, (3)
parse `script` log files with timing information saving output (JSON or HTML)
to a file or dumping to stdout. The last mode is good for converting any old
script sessions to HTML or JSON.

### Special Considerations

`TermRecord` assumes that during a captured session you do not change the
terminal's window size.  This is usually a safe assumption.  However, if you
change the terminal's window size to larger dimensions, rendering in the HTML
may get messed up.  If you resize to smaller dimensions, you should be safe.

We could try and trap window resize events when wrapping `script`, but it is
difficult to merge the timing of that event with the timing information
recorded by `script`.  Thus, we punt this difficulty onto you.  Don't resize
your windows ;-)

## Why?

How do you *share your command line adventures* with your friends? For me, the
best method was crowding around my monitor so I can show them exactly what I
found. But, this isn't scalable or easily recorded for future reference.

How do you *explain to someone remotely how to get started programming*? You
want to show them how to use the tool chain, writing the source code,
debugging, etc. For me, the best method would be sharing terminal sessions, or
using a screen sharing solution like Google Hangouts. But, that requires
real-time interaction and it's hard to reference in the future. You might just
want to show someone what you did to help them debug an issue in their code.

How do you *remember useful commands and how to use them*? Too often I
rely on my own brain expecting it to be a sponge for command line knowledge.
But, this isn't really scalable and my memory is fallible. Other people write
articles and take notes, but it's hard to capture what a tool's inputs and
outputs look like, potential failure messages, and proper execution.

Sure, we have screencasts, terminal sharing solutions, screen sharing
solutions, and even terminal replay services like showterm. But what we're
lacking is a method of archiving our terminal sessions that is cross-platform,
replayable, and easily disseminated without needing a web service in the
middle. Tools like `script` and `scriptreplay` are great, but they aren't
cross-platform.  Videos would be ideal, except you can't easily copy and paste
from them.

Enter TermRecord! TermRecord consumes output from the `script` command with
timing information and can create a self-contained HTML file which replays the
recorded session without needing to load anything from the web. These term
sessions can be emailed and viewed on practically any device (tested on things
like iPads etc.). Basically, the consumer only needs a modern browser.

## Dependencies

TermRecord depends on three things currently:

1. term.js -- minified (YUI), base64 encoded, and embedded in the static
   template; MIT License
2. Google Web Fonts (specifically 'Ubuntu Mono' by default) -- base64 encoded
   and embedded in the static template; Ubuntu Font License 1.0
3. Jinja2 -- Python templating engine; BSD License

## License

TermRecord is licensed under the MIT License. The code must be distributed
with that license intact; however, produced HTML files do not need to include
the license at all.
