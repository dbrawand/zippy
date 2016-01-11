#!/usr/bin/env python

from zippylib.primer import Primer, PrimerPair
import time

'''recursive function to flatten arbitrarily nested containers (list,tuples)'''
def flatten(container):
    # put in a list if it isn't
    if type(container) is not list and type(container) is not tuple and type(container) is not PrimerPair:
        yield container
    else:
        for i in container:
            if isinstance(i, list) or isinstance(i, tuple):
                for j in flatten(i):
                    yield j
            else:
                yield i

'''returns common prefix (substring)'''
def commonPrefix(left,right,stripchars='-_ ',commonlength=3):
    matchingPositions = [ i+1 for i,j in enumerate([ i for i, x in enumerate(zip(left,right)) if len(set(x)) == 1]) if i==j]
    if matchingPositions and max(matchingPositions) >= commonlength:
        return left[:max(matchingPositions)].rstrip(stripchars)
    else:
        return None

'''exception class for configuration errors'''
class ConfigError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "[!] CONFIGURATION ERROR\n\t", repr(self.value)


'''simple progress bar with time estimation'''
class Progressbar(object):
    def __init__(self,total,name='',maxlen=50,char='|'):
        self.start = time.time()
        self.total = total
        self.name = name
        self.maxlen = maxlen
        self.char = char

    def show(self,i):
        if i == 0:
            self.start = time.time()  # set new start time
        eta = str(int((self.total-i)*float(time.time()-self.start)/float(i))) if i/float(self.total)>0.05 else '?'
        return ("{name:} [{progress:<"+str(self.maxlen)+"}] {done:} (ETA {eta:>2}s)").format(\
            name=self.name, progress=self.char*int(self.maxlen*i/float(self.total)), done=str(i)+'/'+str(self.total), eta=eta)
