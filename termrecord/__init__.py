# -*- coding: utf-8 -*-
# vim: set nospell:
##############################################################################
# termrecord/__init__.py                                                     #
#                                                                            #
# init file for termrecord package.                                          #
#                                                                            #
#                                                                            #
#   Authors: Wolfgang Richter <wolfgang.richter@gmail.com>                   #
#                                                                            #
#                                                                            #
#   Copyright 2014-2017 Wolfgang Richter and licensed under the MIT License. #
#                                                                            #
##############################################################################

from os.path import dirname, join

def templated():
    return join(dirname(__file__), 'templates')
