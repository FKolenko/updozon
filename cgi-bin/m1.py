import cgi
form=cgi.FieldStorage()
print ('Content-type: text/html\n')
print ('<title>Reply Page</title>')

import os
# Import modules for CGI handling
import cgi, cgitb
import urllib.request

# enable debugging
cgitb.enable()
# print content type
print("Content-type:text/html\r\n\r\n")
