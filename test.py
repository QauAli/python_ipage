#!/usr/bin/python
import sys
import traceback
print "Content-type: text/html\n\n"
print "<html><head>"
print "<title>CGI Test</title>"
print "</head><body>"
print "<H1>Test page using Python</H1>"

VERSION = sys.version_info
print "<br> Python Version:"
print VERSION
print "<br>"

try:
    import django
    print "<br> Django Version:"
    print django.VERSION
    print "<br>"
except:
    print "<br> Django was not loaded here is the traceback:<br>"
    print traceback.format_exc()
    print "<br>"

try:
    import flask
    print "<br> Flask Version:"
    print flask.__version__
    print "<br>"    
except:
    print "<br> Flask was not loaded here is the traceback:<br>"
    print traceback.format_exc()
    print "<br>"

print "</body></html>"
