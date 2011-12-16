#!/usr/bin/python

""" This is the part which gets the results we want """

import troll

def getResponse(st):
	n = troll.master.index(st)
	return troll.jumbo[n]
