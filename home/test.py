import os


x = os.getcwd()
y = os.path.join( x , 'media/').replace('\\','/')
print x
print y
# print "getcwd: %s" % os.getcwd()
# print "basename: %s" % os.path.basename(__file__)
# print "abspath: %s" % os.path.abspath(__file__)
# print "dirname: %s" % os.path.dirname(os.path.dirname(__file__))