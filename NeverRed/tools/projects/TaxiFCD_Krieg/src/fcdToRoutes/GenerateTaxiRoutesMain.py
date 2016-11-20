#!/usr/bin/env python
# -*- coding: Latin-1 -*-
"""
@file    GenerateTaxiRoutesMain.py
@author  Sascha Krieg
@author  Daniel Krajzewicz
@author  Michael Behrisch
@date    2008-04-17
@version $Id: GenerateTaxiRoutesMain.py 18096 2015-03-17 09:50:59Z behrisch $

Main of GenerateTaxiRoutes.

SUMO, Simulation of Urban MObility; see http://sumo.dlr.de/
Copyright (C) 2008-2015 DLR (http://www.dlr.de/) and contributors

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

from GenerateTaxiRoutes import *


def main():
    print "start program"
    readFCD()
    writeRoutes()
    print "end"

# start the program
main()
