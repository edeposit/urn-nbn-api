#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from registrar import _both_set_and_different


# Functions & classes =========================================================
class DigitalLibrary(object):
    def __init__(self, uid, name, description=None, url=None, created=None):
        self.url = url
        self.uid = uid
        self.name = name
        self.created = created
        self.description = description

    def __eq__(self, other):
        if self.uid != other.uid or self.name != other.name:
            return False

        return not any([
            _both_set_and_different(self.description, other.description),
            _both_set_and_different(self.url, other.url),
            _both_set_and_different(self.created, other.created),
        ])

    def __ne__(self, other):
        return not self.__eq__(other)
