__author__ = 'alessandro'
import random
import string


print "choose the length of the password"
l = int(raw_input(">  "))

key = ''
for i in range(l):
    key += random.choice(string.lowercase + string.uppercase + string.digits)
print 'key: ', key






