#!/usr/bin/python

""" This is the part which gets the results we want """

import troll
import random


def pickFromList(st):
	""" Given a list st, pick a single response """
	l=len(st)
	n=random.randint(0,(l-1))
	res=st[n]
	return res

def getResponseForWord(st):
	""" Given a single word, give a response or nothing if there is none. """
	try:
		word=troll.master[st]
	except:
		return ""
	return pickFromList(word)

def getResponse(st):
	""" Given a sentence, get a response. """
	l = st.split()
	for x in l:
		res=getResponseForWord(x)
		return res 

""" The notion is that we are given a whole email which has many paragraphs in it. 
    First we chunk into a list of paragraphs. Each paragraph is checked for a possible respnose.
    Once we have this, we can reply to that whole paragraph based upon a single key word. """

def paragraph2chunks(st):
	""" FIXME:  Given a string of paragraphs, return a list of paragraphs. """
	return st

def getResponseForParagraphs(st):
	""" FIXME: Given a string of paragraphs, return a single paragraph and an argument
	    for a responose. """
	return st

# Mon Jan  9 21:00:16 PST 2012
