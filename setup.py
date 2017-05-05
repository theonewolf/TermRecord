"""
TermRecord
----------

TermRecord is a program that wraps the ``script`` command.  It automagically
detects your terminal size, records your session, and stores the output as
either JSON, embeddable JavaScript, or a static HTML file.  The HTML is
completely self-contained, embedding all necessary dependencies in one file
and can be shipped to anyone that has a modern browser.  It even embeds a
font!

You can store these files as your own notes, email them to collaborators,
use them as instructional examples, or whatever you want!  Because they are
self-contained there are no third-party middlemen involved, you are free to
share and keep them forever---they will never go away!

Easy to Install
```````````````

.. code:: bash

    $ pip install TermRecord

Super Easy to Use
`````````````````

.. code:: bash

    $ TermRecord -o /tmp/test.html
    $ # do whatever you want, once you exit your shell:
    $ google-chrome /tmp/test.html

Links
`````

* `Development <https://github.com/theonewolf/TermRecord>`_
* `Issue Tracker <https://github.com/theonewolf/TermRecord/issues>`_

"""



from setuptools import setup, find_packages

setup(
    name='TermRecord',
    version='1.2.5',
    url='http://github.com/theonewolf/TermRecord',
    license='MIT',
    author='Wolfgang Richter',
    author_email='wolfgang.richter@gmail.com',
    description='A simple terminal session recorder with easy-to-share '
                'HTML output!',
    long_description=__doc__,
    scripts = ['bin/TermRecord'],
    packages=find_packages(),
    package_data = {'termrecord' : ['FONT-LICENSE',
                                    'LICENSE',
                                    'templates/dynamic.jinja2',
                                    'templates/base.jinja2',
                                    'templates/static.jinja2']},
    install_requires=[
        'Jinja2>=2.6'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Logging',
        'Topic :: Terminals'
    ]
)
