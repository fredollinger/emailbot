#!/usr/bin/python

import sys
import engine

arg="argument Multi \n line \n argument \n bob."

res=engine.getResponse(arg)

if ("" == res):
	print "Nothing to argue about."
	sys.exit()

print engine.getResponse("greeting")
print "\n"
print 'You stated: "%s"' % arg
print "\n"
print engine.getResponse(arg)
print "\n"
print engine.getResponse("closing")
print "\n"
print "Mr. John Chabot"
