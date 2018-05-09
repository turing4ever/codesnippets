#There are currently 3 different protocols which can be used for pickling.
#    Protocol version 0 is the original ASCII protocol and is backwards compatible with earlier versions of Python.
#    Protocol version 1 is the old binary format which is also compatible with earlier versions of Python.
#    Protocol version 2 was introduced in Python 2.3. It provides much more efficient pickling of new-style classes.
#If a protocol is not specified, protocol 0 is used. If protocol is specified as a negative value or HIGHEST_PROTOCOL, the highest protocol version available will be used.

with open('fname.pkl', 'wb') as f:
    cPickle.dump(obj, f, protocol=cPickle.HIGHEST_PROTOCOL)

with open('fname.pkl', 'rb') as f:
    obj = cPickle.load(f) 


# in pactice, the latest protocol 2 is way more efficient than the default protocol 0
#http://dhaneshr.net/2015/09/12/speeding-up-data-serialization-in-python/

