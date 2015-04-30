#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from collections import namedtuple


# Functions & classes =========================================================
class Catalog(namedtuple("Catalog", ["uid",
                                     "name",
                                     "created",
                                     "url_prefix"])):
    """
    Class used for representing informations about Catalogs, where the URN:NBN
    points.
    """
