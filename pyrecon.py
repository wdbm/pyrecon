################################################################################
#                                                                              #
# pyrecon                                                                      #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides configuration reading and parsing utilities in Python. #
#                                                                              #
# copyright (C) 2014 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

version = "2016-01-12T1811Z"

import re
from collections import OrderedDict

def Markdown_list_to_dictionary(Markdown_list):
    line = re.compile(r"( *)- ([^:\n]+)(?:: ([^\n]*))?\n?")
    depth = 0
    stack = [{}]
    for indent, name, value in line.findall(Markdown_list):
        indent = len(indent)
        if indent > depth:
            assert not stack[-1], "unexpected indent"
        elif indent < depth:
            stack.pop()
        stack[-1][name] = value or {}
        if not value:
            # new branch
            stack.append(stack[-1][name])
        depth = indent
    return stack[0]

def Markdown_list_to_OrderedDict(Markdown_list = None):
    line = re.compile(r"( *)- ([^:\n]+)(?:: ([^\n]*))?\n?")
    depth = 0
    stack = [OrderedDict()]
    for indent, name, value in line.findall(Markdown_list):
        indent = len(indent)
        if indent > depth:
            assert not stack[-1], "unexpected indent"
        elif indent < depth:
            stack.pop()
        stack[-1][name] = value or OrderedDict()
        if not value:
            # new branch
            stack.append(stack[-1][name])
        depth = indent
    return stack[0]

def open_configuration(filename):
    configuration_file = open(filename, "r").read()
    return(Markdown_list_to_dictionary(configuration_file))

def open_configuration(filename = None):
    configuration_file = open(filename, "r").read()
    return Markdown_list_to_OrderedDict(configuration_file)
