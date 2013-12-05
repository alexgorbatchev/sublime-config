import os

LOCAL = '/usr/local/bin:/usr/local/sbin:'
HOME = '/Users/alexgorbatchev'
NVM = '/Users/alexgorbatchev/.nvm/v0.10.5/bin'

# Sublime's default path is
# /usr/bin:/bin:/usr/sbin:/sbin
os.environ['PATH'] += ':'
os.environ['PATH'] += LOCAL
os.environ['PATH'] += NVM

print '\n\n--------------'
print 'pathching path in `User/paths.py`'
print 'PATH = ' + os.environ['PATH']
print '--------------\n'
